# singly linked list implementation
# Covers --
## Inserstion(start, end, after position), Deletion(start, end, position), Traversal

class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def set_next(self,node= None):
		self.next = node
	
	def insert_bw(self, node1, node2=None):
		node1.next = self
		self.next = node2		

	def pprint(self):
		print str(self.data) + "--->",


class LinkedList():
	def __init__(self, head = None, total_nodes = 0):     #head points to the first node
		self.head = head
		self.total_nodes = total_nodes

### Insertion Methods Start ###

	def insert_start(self, value):
		self.total_nodes += 1
		n = Node(value)
		n.set_next(self.head)
		self.head = n
		self.pprint()

	def insert_end(self,value):
		node = self.head
		new_node = Node(value)
		if node == None:
			self.insert_start(value)
		else:
			self.total_nodes += 1
			while node.next!=None:
				node = node.next
			node.set_next(new_node)
			self.pprint()

	def insert_after_position(self,value,position=None):  # insert after a position in list, 1  being first node
		if position==None:
			self.insert_end(value)
		else:
			self.total_nodes += 1
			count = 1
			node = self.head
			new_node = Node(value)
			if position == 1:
				new_node.insert_bw(node, node.next)
			elif position < 1:
				print "Less than 1 means nothing Mate!"
			else:
				while count != position:
					if node == None:
						print "Invalid position given"
						return
					else:	
						count += 1
						node = node.next	
				new_node.insert_bw(node, node.next)
				self.pprint()

### Insertion Methods End ###

### Deletion Methods Start ###
	

	def delete_first(self):
		tmp_node = self.head
		self.head = self.head.next            # could have use the node method as well
		self.delete_node(tmp_node)

	def delete_last(self):
		node = self.head
		if node== None:
			"No items in the list"
		else:
			while node.next!=None:     		  # Moving 1 step ahead to ge the next node first
				second_last_node = node
				node = node.next
			second_last_node.next = None	
			self.delete_node(node)

	def delete_at(self, position):
		node = self.head
		count = 1
		if node == None:
			print "List is Empty"
		else:
			if position == count:
				self.delete_first()
			else:	
				while count != position:
					if node == None:
						print "Invalid poistion"
						return
					previous = node
					node = node.next
					count += 1
				previous.next = node.next
				self.delete_node(node)		

	def delete_node(self,node):               # Generic Method to remove the node from the memory
		self.total_nodes += -1
		print "Deleting the element with data : " + str(node.data)
		del node
		self.pprint()		
			

### Deletion Methods End ###


	def has_value(self,value):
		node = self.head
		count = 1
		if node == None:
			print "List is currently empty"
		else:	
			while node.data != value:
				if node.next == None:
					print "Given Item not in the list"
					return
				node.pprint
				count += 1
				node = node.next
			print "Item found at " + str(count) + " position"	



	def pprint(self):
		print "total nodes = " + str(self.total_nodes)
		node = self.head
		if node == None:
			print "Nothing in the list"
		else:
			while node!=None:
				node.pprint()
				node = node.next			



n=Node(23)
n.pprint()		

s=LinkedList()
s.insert_end(21)
s.insert_end(24)
s.insert_end(25)