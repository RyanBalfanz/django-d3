from django import template
from django.template.loader import render_to_string

register = template.Library()


class D3Node(template.Node):
	"""docstring for D3Node"""
	def __init__(self, values):
		super(D3Node, self).__init__()
		self.values = values
		
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
