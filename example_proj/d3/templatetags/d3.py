import json
import random
import string

from django import template
from django.template.loader import render_to_string


register = template.Library()

def randname(length=6):
	return ''.join(random.choice(string.letters) for i in xrange(length))


class D3Node(template.Node):
	"""docstring for D3Node"""
	def __init__(self, values):
		super(D3Node, self).__init__()
		self.values = values
		self.gid = randname()
		
	def render(self, context):
		"""docstring for render"""
		chart = render_to_string("d3/_d3_test_chart.html", {'data': self.values})
		return chart
		# return '<span>template tag d3_chart</span>'
		# raise NotImplementedError, "Register a tag that returns a subclass of D3Node"


class D3DepsNode(template.Node):
	"""docstring for D3DepsNode"""
	def __init__(self):
		super(D3DepsNode, self).__init__()
		
	def render(self, context):
		"""docstring for render"""
		raise NotImplementedError, "Register a tag that returns a subclass of D3DepsNode"


@register.tag(name="d3_test_chart")
def d3_chart(parser, token):
	"""docstring for d3_chart"""
	try:
		# split_contents() knows not to split quoted strings.
		tag_name, format_string = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
	if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
		raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
	valsAsString = token.split_contents()[1:][0].strip("'").split(',')
	vals = [map(float, valsAsString)]
	return D3Node(vals)


class D3SeriesNode(template.Node):
	"""docstring for D3SeriesNode"""
	def __init__(self, values):
		super(D3SeriesNode, self).__init__()
		self.values = values
		self.gid = randname()
		print self.gid, self.values
		
	def render(self, context):
		"""docstring for render"""
		# print "VALUES:", self.values
		numSeries = 1
		numPoints = 25
		xMax = 1.0
		height = 275
		goldenRatio = 1.61803399
		d = []
		for s in xrange(numSeries):
			for i in xrange(numPoints):
				inner_dict = {"x": i*xMax/numPoints, "y": random.random()}
				d.append(inner_dict)
		d = json.dumps(d)
		print d
		c = {
			"data": d,
			"height": height,
			"width": round(height*goldenRatio),
			# "options": {
			# 	"height": 275,
			# 	"width": 450,
			# }
		}
		chart = render_to_string("d3/_d3_line_chart.html", c)
		return chart


class D3SeriesDepsNode(template.Node):
	"""docstring for D3SeriesDepsNode"""
	pass


@register.tag(name="d3_series_chart")
def d3_series_chart(parser, token):
	"""Template Tag for d3_series_chart (a line chart)"""
	try:
		# split_contents() knows not to split quoted strings.
		bits = token.split_contents()
		tagName, formatString = bits[0], bits[1:]
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
		
	print "Tag Name: {0}".format(tagName)
	print "Format String: {0}, {1}".format(formatString, type(formatString))
	
	numExtraBits = len(formatString)
	if numExtraBits == 1:
		# Only given data
		dataBit = formatString[0]
	elif numExtraBits == 2:
		# Given data and extra options
		dataBit, optsBit = formatString[0], formatString[1]
		
	key, value = dataBit.split('=')
	seriesList = value.split(',')
	print "Key: {0}".format(key)
	print "Value: {0}".format(value)
	print "Series List: {0}".format(seriesList)
	
	return D3SeriesNode(seriesList)


class D3BarNode(template.Node):
	"""docstring for D3BarNode"""
	def __init__(self, values):
		super(D3BarNode, self).__init__()
		self.values = values
		self.gid = randname()
		print self.gid, self.values

	def render(self, context):
		"""docstring for render"""
		# print "VALUES:", self.values
		numSeries = 1
		numPoints = 25
		xMax = 1.0
		height = 275
		goldenRatio = 1.61803399
		d = []
		for s in xrange(numSeries):
			for i in xrange(numPoints):
				inner_dict = {"x": i*xMax/numPoints, "y": random.random()}
				d.append(inner_dict)
		d = json.dumps(d)
		print d
		c = {
			"data": d,
			"height": height,
			"width": round(height*goldenRatio),
			# "options": {
			# 	"height": 275,
			# 	"width": 450,
			# }
		}
		chart = render_to_string("d3/_d3_bar_chart.html", c)
		return chart


@register.tag(name="d3_bar_chart")
def d3_bar_chart(parser, token):
	"""Template Tag for d3_bar_chart (a horizontal bar chart)"""
	try:
		# split_contents() knows not to split quoted strings.
		bits = token.split_contents()
		tagName, formatString = bits[0], bits[1:]
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])

	print "Tag Name: {0}".format(tagName)
	print "Format String: {0}, {1}".format(formatString, type(formatString))

	numExtraBits = len(formatString)
	if numExtraBits == 1:
		# Only given data
		dataBit = formatString[0]
	elif numExtraBits == 2:
		# Given data and extra options
		dataBit, optsBit = formatString[0], formatString[1]

	key, value = dataBit.split('=')
	seriesList = value.split(',')
	print "Key: {0}".format(key)
	print "Value: {0}".format(value)
	print "Series List: {0}".format(seriesList)

	return D3BarNode(seriesList)


class D3PieNode(template.Node):
	"""docstring for D3PieNode"""
	def __init__(self, values):
		super(D3PieNode, self).__init__()
		self.values = values
		self.gid = randname()
		print self.gid, self.values

	def render(self, context):
		"""docstring for render"""
		# print "VALUES:", self.values
		numSeries = 1
		numPoints = 25
		xMax = 1.0
		height = 275
		goldenRatio = 1.61803399
		d = []
		for s in xrange(numSeries):
			for i in xrange(numPoints):
				inner_dict = {"x": i*xMax/numPoints, "y": random.random()}
				d.append(inner_dict)
		d = json.dumps(d)
		print d
		c = {
			"data": d,
			"height": height,
			"width": round(height*goldenRatio),
			# "options": {
			# 	"height": 275,
			# 	"width": 450,
			# }
		}
		chart = render_to_string("d3/_d3_pie_chart.html", c)
		return chart


@register.tag(name="d3_pie_chart")
def d3_pie_chart(parser, token):
	"""docstring for d3_pie_chart"""
	try:
		# split_contents() knows not to split quoted strings.
		bits = token.split_contents()
		tagName, formatString = bits[0], bits[1:]
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])

	print "Tag Name: {0}".format(tagName)
	print "Format String: {0}, {1}".format(formatString, type(formatString))

	numExtraBits = len(formatString)
	if numExtraBits == 1:
		# Only given data
		dataBit = formatString[0]
	elif numExtraBits == 2:
		# Given data and extra options
		dataBit, optsBit = formatString[0], formatString[1]

	key, value = dataBit.split('=')
	seriesList = value.split(',')
	print "Key: {0}".format(key)
	print "Value: {0}".format(value)
	print "Series List: {0}".format(seriesList)

	return D3PieNode(seriesList)
