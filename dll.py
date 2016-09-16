# Doubly Linked List implementations
# Covers - 
## Insertion(start, end , after start position, after end pos), Deletion(start, end, at position), Traversal, Search

class Node(object):
	"""docstring for Node"""
	def __init__(self, data, prev = None, next = None):
		self.data = data
		self.prev = prev
		self.next = next

	def set_next(self, node):			# this single method can be used to set a node as Next(next) or Prevoius(prev)
		self.next = node
		node.prev = self	

	def insert_bw(self, node1, node2= None):
		node1.set_next(self)
		self.set_next(node2)

	def pprint(self):
		print str(self.data) + "<--->",


class DoublyLinkedList(object):
	def __init__(self, head=None, tail=None):     #tail is the last node
		self.head = head;
		self.tail = tail

### Insertion Methods Start

	def insert_start(self, value):
		new_node = Node(value)
		if self.head == self.tail == None:   #refactor these 3 lines from insert methods
			self.head = new_node
			self.tail = new_node
		else:
			new_node.set_next(self.head)
			self.head = new_node
		self.pprint()

	def insert_end(self, value):
		new_node = Node(value)
		if self.head == self.tail == None:
			self.head = new_node
			self.tail = new_node
		else: 
			self.tail.set_next(new_node)
			self.tail = new_node
		self.pprint()

	def insert_after_position(self, value, position):
		count = 1
		node = self.head
		while count != position:
			node = node.next
			if node == None:
				print "Invalid Position"
				return
			else:
				count += 1
		new_node = Node(value)
		if node.next != None:						#check if the next node is not empty for our Node methods to work fine
			new_node.insert_bw(node, node.next)		
		else:
			node.set_next(new_node)
		self.pprint()	

	def insert_before_end(self, value, position):
		count = 1
		node = self.tail
		while count != position:
			node = node.prev
			if node == None:
				print "Invalid Position"
				return
			else:
				count += 1
		new_node = Node(value)
		if node.prev != None:						#check if the previous node is not empty. Just like above
			new_node.insert_bw(node.prev, node)		
		else:
			new_node.set_next(node)
		self.pprint()	
				
### Insertion Methods End

		
	def pprint(self):
		node = self.head
		if self.head == self.tail == None:
			print "Nothing in the list"
		else:
			print "Head--->",
			while node != None:
				node.pprint()
				node = node.next
			print "Tail"	

d= DoublyLinkedList()
d.insert_start(21)
d.insert_start(29)						
d.insert_start(18)						
d.insert_end(24)						





