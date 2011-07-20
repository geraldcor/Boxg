from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from boxg.home.models import Artists, ArtistImages, Exhibition, SubmissionPDF, Hours, MyFlatPage
		
# class TweakedFlatPageAdmin(FlatPageAdmin):
# 	
# 	def get_form(self, request, obj=None, **kwargs):
# 		if request.user.is_superuser:
# 			self.readonly_fields = ()
# 		else:
# 			self.readonly_fields = ('url', 'sites', 'enable_comments', 'template_name',  'registration_required')
# 		return super(TweakedFlatPageAdmin, self).get_form(request, obj=None, **kwargs)
# 
class MyFlatPageForm(FlatpageForm):
	image1_caption = forms.CharField(widget=forms.Textarea(), required=False)
	image2_caption = forms.CharField(widget=forms.Textarea(), required=False)
	class Meta:
		model = MyFlatPage
	
class MyFlatPageAdmin(FlatPageAdmin):
	form = MyFlatPageForm
	fieldsets = (
	(None, {'fields': ('url', 'title', 'template_name', 'content', 'sites',
			'image1', 'image1_caption', 'x1', 'y1',
			'image2', 'image2_caption', 'x2', 'y2')}),
	 )
	verbose_name = 'My Flat Page'
	verbose_name_plural = 'My Flat Pages'
	
admin.site.unregister(FlatPage)
admin.site.register(MyFlatPage, MyFlatPageAdmin)

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            width = value.width
            height = value.height
            if width > height:
            	scaled_width = 80
            	xwidth = width / 80
            	scaled_height = height / xwidth
            else:
                if height > 80:
                    scaled_height = 80
                    xheight = height / 80
                    scaled_width = width / xheight
                else:
                    scaled_height = height
                    xheight = height
                    scaled_width = width
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="%spx" height="%spx" /></a> %s ' % (image_url, image_url, file_name, scaled_width, scaled_height, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ArtistImagesInline(admin.TabularInline):
	model = ArtistImages
	readonly_fields = ('width', 'height',)
	extra = 8
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'image':
			request = kwargs.pop("request", None)
			kwargs['widget'] = AdminImageWidget
			return db_field.formfield(**kwargs)
		return super(ArtistImagesInline,self).formfield_for_dbfield(db_field, **kwargs)


class ArtistsAdmin(admin.ModelAdmin):
	inlines = [ArtistImagesInline,]
	readonly_fields = ('width', 'height',)
	
	class Media:
		js = ('js/custom_admin.js',)
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'avatar':
			request = kwargs.pop("request", None)
			kwargs['widget'] = AdminImageWidget
			return db_field.formfield(**kwargs)
		return super(ArtistsAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Artists, ArtistsAdmin)

class SubmissionPDFAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(SubmissionPDF, SubmissionPDFAdmin)

class ExhibitionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Exhibition, ExhibitionAdmin)

class HoursAdmin(admin.ModelAdmin):
	pass

admin.site.register(Hours, HoursAdmin)
