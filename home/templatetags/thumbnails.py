import os
import Image
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

def thumbnail(file, size='104x104'):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url

register.filter(thumbnail)

def htmlsize(img, constraint):
	"""
	The constraint is the size in pixels you want to be the max image size
	400w means 400px wide
	400h means 400px high
	"""
	if constraint.find('w'):
		width = constraint.replace('w','')
		xwidth = float(img.width) / float(width)
		height = int(float(img.height) / float(xwidth))
	else:
		height = constraint.replace('h','')
		xheight = float(img.height) / float(height)
		width = float(img.width) / float(xheight)
	return mark_safe('width="%s" height="%s"' % (width, height))
htmlsize.is_safe = True
register.filter(htmlsize)

def get_drilldown(archives):
	html = '<ul id="drilldown">'
	for k,v in archives.items():
		html += '<li><span class="clickable">%s</span>' % k
		html += "<ul>"
		for item in v:
			try:
				item[1]
				html += '<li><span class="clickable">%s</span><ul>' % item[0]
				html += '<li><a href="/past/%s/">%s</a></li>' % (item[1][0], item[1][1])
				html += '</ul>'
			except:
				html += '<li>%s</li>' % item[0]
		html += "</ul>"
		"</li>"
	"</ul>"
	return mark_safe(html)
get_drilldown.is_safe = True
register.filter(get_drilldown)

