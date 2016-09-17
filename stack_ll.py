## Stack Implementation using Linked list
### Covers -
##

class Node(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

	def pprint(self):
		print "|              ^"	+ str(self.data) 
		
class Stack(object):
	"""docstring for Stack"""
	def __init__(self, limit = 1):
		self.limit = limit
		self.top = None
		self.size = 0

	def	push(self, value):
   		node = Node(value)
		if self.size == self.limit:
			print "Stack Overflow"
		else:
			self.size += 1
			node.next = self.top
			self.top = node
		self.pprint()	

	def pop(self):
		if self.size == 0:
			print "Stack Underflow"
		else:
			self.size -= 1
			tmp = self.top
			self.top = self.top.next
			del tmp
		self.pprint()	

	def pprint(self):
		node = self.top
		print "-------------> Top <------------"
		while node != None:
			node.pprint()
			node = node.next
		print "================================"


s=Stack(3)
s.push(29)
s.push(90)
s.push(12)
s.push(22)

##Sample Output
# >>> execfile('stack_ll.py')
# -------------> Top <------------
# |              ^29
# ================================
# -------------> Top <------------
# |              ^90
# |              ^29
# ================================
# -------------> Top <------------
# |              ^12
# |              ^90
# |              ^29
# ================================

# Stack Overflow
# -------------> Top <------------
# |              ^12
# |              ^90
# |              ^29
# ================================



# >>> s.pop()
# -------------> Top <------------
# |              ^90
# |              ^29
# ================================

# >>> s.pop()
# -------------> Top <------------
# |              ^29
# ================================

# >>> s.pop()
# -------------> Top <------------
# ================================

# >>> s.pop()
# Stack Underflow
# -------------> Top <------------
# ================================







				
			


