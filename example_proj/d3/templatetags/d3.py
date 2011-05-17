from django import template
from django.template.loader import render_to_string
import random
import string

# from settings import STATIC_URL

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
		print "VALUES:", self.values
		d = {'x': [0.1, 0.2, 0.3], 'y': [1.2, 1.3, 1.4]}
		# {x: i / 19, y: (Math.sin(i / 3) + 1) / 2}
		chart = render_to_string("d3/_d3_line_chart.html", {'data': d})
		return chart
		# return '<span>template tag d3_chart</span>'
		# raise NotImplementedError, "Register a tag that returns a subclass of D3Node"


class D3SeriesDepsNode(template.Node):
	"""docstring for D3SeriesDepsNode"""
	pass


@register.tag(name="d3_series_chart")
def d3_series_chart(parser, token):
	"""docstring for d3_bar_chart"""
	try:
		# split_contents() knows not to split quoted strings.
		tagName, formatString = token.split_contents()
		# print tag_name, format_string
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
		
	# if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
	# 	raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
		
	print tagName, formatString
	key, value = formatString.split('=')
	seriesList = value.split(',')
	print key, value, seriesList
	return D3SeriesNode(seriesList)
