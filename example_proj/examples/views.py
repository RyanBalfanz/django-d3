import datetime
import math

# from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	now = datetime.datetime.now()
	return render_to_response('examples/index.html', {"now": now})

def bar_chart(request):
	"""bar chart view"""
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	return render_to_response('examples/bar_chart.html', {'series': sqrt})

def line_chart(request):
	"""line chart view"""
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	return render_to_response('examples/line_chart.html', {'series': sqrt})

def pie_chart(request):
	"""pie_chart view"""
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	return render_to_response('examples/pie_chart.html', {'series': sqrt})

def examples(request):
	now = datetime.datetime.now()
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	# return render_to_response('d3/examples.html')
	return render_to_response('d3/examples.html', {'now': now, 'series': sqrt, 'data': sqrt})
