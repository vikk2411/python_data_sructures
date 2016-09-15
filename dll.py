# Doubly Linked List implementations
# Covers - 
## 

class Node(object):
	"""docstring for Node"""
	def __init__(self, data, prev = None, next = None):
		self.prev = prev
		self.next = next

	def pprint(self):
		print str(self.data) + "<--->"

