# BST implementation
# Covers --
# Instertion, Traversal(reorder change the type), Searching
## Needs code imprvement in insertion(few redundant lines)

import random # to fill in the random values in tree

class Node:
	def __init__(self,data = None,parent = None,left = None,right=None):
		self.data = data
		self.parent = parent
		self.left = left
		self.right = right


	def set_parent(self, parent):
		self.parent = parent

	def is_root(self):
		print  self.parent==None

	def set_left(self,node):
		self.left = node
		node.parent = self

	def set_right(self,node):
		self.right = node
		node.parent = self		

	#reordering the below function will change the way we traverse the tree, although all will work just fine	
	def print_tree(self):
		self.print_left()
		self.print_as_tree(),
		self.print_right()
		count = 1

	def print_as_tree(self):
		if self.left != None and self.right != None:
			print str(self.data) + "--(" + str(self.left.data) + "," + str(self.right.data) + ") ===>",	
		elif self.left == None and 	self.right != None:
			print str(self.data) + "--(??" + "," + str(self.right.data) + ") ===>",	
		elif self.left != None and 	self.right == None:
			print str(self.data) + "--(" + str(self.left.data) + "," + "??) ===>",	
		else:
			print str(self.data) + "--(??,??) ---->",	

	def print_left(self):
		if self.left != None:
			self.left.print_tree()
		else:
			# print "No left child for " + str(self.data)
			pass

	def print_right(self):
		if self.right != None:
			self.right.print_tree()
		else:
			# print "No right child for " + str(self.data)
			pass	

	def has_value(self,value):
		# self.print_as_tree()       
		print str(self.data) + "--->",
		if value == self.data:
			print "Tree contains this value"
		elif value < self.data:
			self.search_left(value)
		elif value > self.data:
			self.search_right(value)
		else:
			print "Whatta joke ============"			
	
	def search_left(self,value):
		if self.left != None:
			self.left.has_value(value)
		else:
			print "No values found-- Left side end"	

	def search_right(self,value):
		if self.right != None:
			self.right.has_value(value)
		else:
			print "No values found-- Right side end"			


n=Node(21)
n1=Node(23)
n.print_as_tree()
# n.is_root()
n.set_left(n1)
n1.print_as_tree()
# n1.is_root()
n.print_as_tree()


class BST():
	def __init__(self,root=None):
		self.root = root  #this mst be a node

	def insert_left(self,node,value):
		if node.left == None:
			new_node = Node(value)
			node.set_left(new_node)
			node.print_as_tree()
			new_node.print_as_tree()
			# return new_node
		else:
			self.insert(value, node.left)

	def insert_right(self,node,value):
		if node.right == None:
			new_node = Node(value)
			node.set_right(new_node)
			node.print_as_tree()
			new_node.print_as_tree()
			# return new_node
		else:
			self.insert(value, node.right)				

	def insert(self,value, node = None):
		if node == None:
			if self.root == None:
				self.root = Node(value)
				self.root.print_as_tree()
			else:
				self.insert(value, self.root)	
		elif value < node.data:
			self.insert_left(node, value)
		elif value > node.data:
			self.insert_right(node,value)
		else:
			print "Values are equal"

	def find_tree(self,value):
		if self.root == None:
			print "No Nodes in the tree"
		else:
			self.root.has_value(value)

	def print_tree(self):
		if self.root == None:
			print "No Nodes in the tree"
		else:
			self.root.print_tree()			



b=BST()
b.insert(28)
b.insert(32)
b.insert(26)
b.insert(30)
b.insert(29)
b.insert(25)
b.insert(24)
b.insert(27)
for n in range(0,20):
	b.insert(random.randint(10,80))
