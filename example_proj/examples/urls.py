from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'example_proj.examples.views.home', name='examples_home'),
	url(r'^time-series/$', 'example_proj.examples.views.random_series', name='random-series'),
	url(r'^bar/$', 'example_proj.examples.views.bar_chart', name='bar-chart'),
	url(r'^line/$', 'example_proj.examples.views.line_chart', name='line-chart'),
	url(r'^pie/$', 'example_proj.examples.views.pie_chart', name='pie-chart'),
)
