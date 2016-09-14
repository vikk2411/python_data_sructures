# singly linked list implementation
# Covers --
## Inserstion(start, end, after position), traveral

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
	def __init__(self, head = None):     #head points to the first node
		self.head = head

	def insert_start(self, value):
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
			while node.next!=None:
				node = node.next
			node.set_next(new_node)
			self.pprint()

	def insert_after_position(self,value,position=None):  # insert after a position in list, 1  being first node
		if position==None:
			self.insert_end(value)
		else:
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
						print "Invalid position give"
						break
					else:	
						count += 1
						node = node.next	
				new_node.insert_bw(node, node.next)
				self.pprint()



	def pprint(self):
		node = self.head
		if node == None:
			print "Nothing in the list"
		else:
			while node!=None:
				node.pprint()
				node = node.next			



n=Node(23)
n.pprint()		