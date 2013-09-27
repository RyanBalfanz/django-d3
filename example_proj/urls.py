from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'example_proj.examples.views.home', name='home'),
	url(r'^d3/', include('example_proj.d3.urls')),
	url(r'^examples/', include('example_proj.examples.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
)
