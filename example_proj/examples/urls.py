from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^$', 'examples.views.home', name='examples_home'),
	url(r'^bar/$', 'examples.views.bar_chart', name='bar-chart'),
	url(r'^line/$', 'examples.views.line_chart', name='line-chart'),
	url(r'^pie/$', 'examples.views.pie_chart', name='pie-chart'),
)
