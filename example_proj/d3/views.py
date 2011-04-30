import datetime

# from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	now = datetime.datetime.now()
	return render_to_response('d3/index.html', {"now": now})

def examples(request):
	now = datetime.datetime.now()
	return render_to_response('d3/examples.html')
	# return render_to_response('d3/examples.html', {"now": now})

def easter_egg(request):
	now = datetime.datetime.now()
	return render_to_response('d3/easter_egg.html', {"now": now})
