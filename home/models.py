from django.db import models
from django.contrib.flatpages.models import FlatPage

def get_upload_path(instance, filename):
	"""
	Return the path to upload images. Saves the images to the Artists pk subfolder
	"""
	return 'artist_images/%d/%s' % (instance.artists.id, filename)

class Artists(models.Model):
	name = models.CharField(max_length=255)
	avatar = models.ImageField(upload_to='images/avatars', 
max_length=255, height_field='height', width_field='width')
	height = models.IntegerField(blank=True, null=True)
	width = models.IntegerField(blank=True, null=True)
	hide = models.BooleanField('Hide Artist', blank=True, help_text='Hide this artist on the page listing all artists. Useful for group exhibitions.')
	statement = models.TextField(blank=True)
	resume = models.TextField(blank=True)
	
	def __unicode__(self):
		return u'%s' % self.name
		
	class Meta:
		verbose_name_plural = 'Artists'
	
class ArtistImages(models.Model):
	artists = models.ForeignKey(Artists)
	order = models.IntegerField(help_text='Image Display Order')
	image = models.ImageField(upload_to=get_upload_path, 
max_length=255, height_field='height', width_field='width')
	caption = models.CharField(max_length=255, blank=True)
	height = models.IntegerField(blank=True, null=True)
	width = models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		return u'%s' % self.caption
	
	class Meta:
		verbose_name_plural = 'Artist Images'
		ordering = ['order']

class Exhibition(models.Model):
	name = models.CharField('Title', max_length=255, blank=True)
	artists = models.ForeignKey(Artists)
	video_link = models.CharField(max_length=255, blank=True, 
help_text='Paste the <strong>Embed</strong> link from your YouTube video. It should look like <iframe...')
	dates_info = models.TextField()
	begin_date = models.DateField(help_text='This is the date the exhibition will be put on the homepage.')
	end_date = models.DateField(help_text='This is the date the exhibition will drop off the homepage')
	
	def __unicode__(self):
		return u'%s' % self.name
		
class SubmissionPDF(models.Model):
	pdf_file = models.FileField(upload_to='submission')
	
	def __unicode__(self):
		return u'%s' % self.pdf_file
	
	class Meta:
		verbose_name = 'Submission Form'
		verbose_name_plural = 'Submission Forms'

class Hours(models.Model):
	hours = models.CharField(max_length=255, blank=True, help_text='This is shown on the Contact Page.')
	
	def __unicode__(self):
		return u'%s' % self.hours

	class Meta:
		verbose_name = 'Box Gallery Hours'
		verbose_name_plural = 'Box Gallery Hours'
		
class MyFlatPage(FlatPage):
	image1 = models.ImageField(upload_to='myflatpages', 
max_length=255, height_field='y1', width_field='x1', blank=True)
	image1_caption = models.CharField(max_length=300, blank=True)
	y1 = models.IntegerField(blank=True, null=True)
	x1 = models.IntegerField(blank=True, null=True)
	image2 = models.ImageField(upload_to='myflatpages', 
max_length=255, height_field='y2', width_field='x2', blank=True)
	image2_caption = models.CharField(max_length=300, blank=True)
	y2 = models.IntegerField(blank=True, null=True)
	x2 = models.IntegerField(blank=True, null=True)
