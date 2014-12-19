class BinaryTreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def get_left(self):
		if self.left != None:
			return self.left
		else:
			return None

	def set_left(self, node):
		if self.get_left(self) == None:
			# if there is nothing to the left place the node there
			self.left = node
			return
		else:
			# if there is something to the left, move your pointer to that node on the left 
			# and recursively check if there is anything to the left of that
			return (self.left).set_left(node)

	def get_right(self):
		if self.right != None:
			return self.right
		else: 
			return None

	def set_right(self, node):
		if self.get_right(self) == None:
			return
		else:
			return (self.right).set_right(node)

	def get_value(self):
		return self.value

	def set_value(self, number):
		if self.get_value(self) == None:
			self.value = number

	def depth_first_traversal(node):
    pass