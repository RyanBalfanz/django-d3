import datetime
import math

# from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	now = datetime.datetime.now()
	dt = datetime.timedelta(days=1)
	today = datetime.date.today()
	series = [i*0.1 for i in range(10)]
	timeSeries = map(str, [today - i*dt for i in reversed(range(10))])
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	data = {'x': series, 'y': sqrt}
	timeSeriesData = {'x': timeSeries, 'y': sqrt}
	return render_to_response('examples/index.html', {"now": now})

def examples(request):
	now = datetime.datetime.now()
	dt = datetime.timedelta(days=1)
	today = datetime.date.today()
	series = [i*0.1 for i in range(10)]
	timeSeries = map(str, [today - i*dt for i in reversed(range(10))])
	sqrt = [math.sqrt(i*0.1) for i in range(10)]
	data = {'x': series, 'y': sqrt}
	timeSeriesData = {'x': timeSeries, 'y': sqrt}
	# return render_to_response('d3/examples.html')
	return render_to_response('d3/examples.html', {'now': now, 'series': sqrt, 'data': sqrt})

def easter_egg(request):
	now = datetime.datetime.now()
	return render_to_response('d3/easter_egg.html', {"now": now})
