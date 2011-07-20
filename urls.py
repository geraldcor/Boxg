from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^', include('boxg.home.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	# favico from google search
	(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/home/boxgallery/webapps/media/images/favicon.ico'}),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/boxgallery/webapps/media'}),
		#(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/gregcorey/Dropbox/Code/boxg/static'}),
	)
