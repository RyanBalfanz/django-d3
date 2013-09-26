from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^easter-egg/$', 'example_proj.d3.views.easter_egg', name='easter-egg'),
)

urlpatterns += staticfiles_urlpatterns()
