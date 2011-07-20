from django.conf.urls.defaults import *

urlpatterns = patterns('boxg.home.views',
    (r'^$', 'index'),
	(r'^artists/$', 'artists'),
	(r'^contact/$', 'contact'),
	(r'^past/$', 'past'),
	(r'^past/(?P<exhibit_id>\d+)/$', 'past'),
	(r'^artist/(?P<art_id>\d+)/$', 'artist'),
#	(r'^bigmap/$', 'bigmap'),
#	(r'^flickr/$', 'flickr_template'),
#	(r'^flickr/callback/$', 'callback'),
#	(r'^archive/$', 'blog_archive'),
#	(r'^twitter/(?P<twitid>\w+)/$', 'twit'),
#	(r'^blog/(?P<id>\d+)/(?P<slug>[-\w]+)/$', 'blog'),
#	(r'^blog/flickr/$', 'flickr'),
#	(r'^blog/flickrid/$', 'flickrid'),
#	(r'^me/(?P<username>[\w]+)/$', 'mine'),
	
)
#urlpatterns += patterns('',
#	(r'^blogarchive/$', 'django.views.generic.date_based.archive_year', {'year':'2010', 'queryset':blog_dict, 'date_field':'timestamp', 'make_object_list':True}),
#)
