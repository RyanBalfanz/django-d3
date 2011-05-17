from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', include('example_proj.examples.urls')),
	url(r'^examples/$', 'example_proj.d3.views.examples', name='examples'),
)
