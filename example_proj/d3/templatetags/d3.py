from django import template

register = template.Library()


class D3Node(template.Node):
	"""docstring for D3Node"""
	def __init__(self):
		super(D3Node, self).__init__()
		
	def render(self, context):
		"""docstring for render"""
		pass


class D3DepsNode(template.Node):
	"""docstring for D3DepsNode"""
	def __init__(self):
		super(D3DepsNode, self).__init__()
		
	def render(self, context):
		"""docstring for render"""
		pass


@register.tag()
def bar_chart(parser, token):
	"""docstring for bar_chart"""
	pass
	return ''
