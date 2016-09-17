# Doubly Linked List implementations
# Covers - 
## Insertion(start, end , after start position, after end pos), Deletion(start, end, at position), 
## Traversal(back and forth) and Search

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


### Deletion Methods End

# Start and End are similiar implementation so skipping the later one
	def delete_first(self):
		node = self.head
		if self.head == self.tail == None:
			"Nothing in the list"
		else:
			self.head = node.next
			self.head.prev = None
			self.delete_node(node)

	def delete_at_position(self, position):
		node = self.head
		if self.head == self.tail == None:
			"Nothing in the list"
		else:
			count = 1                  # Use 0 for removing after the position
			while count != position:
				node = node.next
				if node	== None:
					print "Invalid Position"
					return
				else:
					count += 1
			if node.prev != None:	
				node.prev.next = node.next
			if node.next != None:
				node.next.prev = node.prev
			self.delete_node(node)					

	def delete_node(self,node):               # Generic Method to remove the node from the memory
			if node == self.head == self.tail:
				self.head = self.tail = None
			elif node == self.head:
				self.head = node.next
			elif node == self.tail:
				self.tail = node.prev		
			print "Deleting the element with data : " + str(node.data)
			del node
			self.pprint()

### Deletion Methods End

### Search
	def has_value(self,value):
		node = self.head
		count = 1
		if node == self.tail == None:
			print "List is currently empty"
		else:	
			while node.data != value:
				if node.next == None:
					print "\nGiven Item not in the list"
					return
				node.pprint()
				count += 1
				node = node.next
			print "\nItem found at " + str(count) + " position"	




## Travesal(forth)		
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


## Travesal(forth)		
	def pprint_reverse(self):
		node = self.tail
		if self.head == self.tail == None:
			print "Nothing in the list"
		else:
			print "Tail<---",
			while node != None:
				node.pprint()
				node = node.prev
			print "Head"


## Populate the list with random data
d= DoublyLinkedList()
d.insert_start(21)
d.insert_start(29)						
d.insert_start(18)						
d.insert_end(24)						





