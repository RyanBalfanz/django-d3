from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'example_proj.d3.views.home', name='home'),
    url(r'^examples/$', 'example_proj.d3.views.examples', name='examples'),
    url(r'^easter-egg/$', 'example_proj.d3.views.easter_egg', name='easter-egg'),
    # url(r'^example_proj/', include('example_proj.foo.urls')),
    # url(r'^example_proj/', include('example_proj.d3.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
