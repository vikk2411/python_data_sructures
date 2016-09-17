## Stack Implementation using Arrays
# We know arrays as Lists in python, but we will use Array word only. Dont confuse.
### Covers - 
## Insert, Delete, Display

class Stack(object):
	"""docstring for Stack"""
	def __init__(self, limit, array = []):
		self.array = array
		self.limit = limit
		self.top = None
		self.size = len(self.array)
		self.set_top()
		self.pprint()

	def set_top(self):
		if self.array == []:
			self.top = None
		else:
			self.top = self.array[-1]

	def is_full(self):
		return self.size == self.limit

	def is_empty(self):
		return self.size == 0			

	def push(self, value):
		if self.size == self.limit:
			print "Stack Overflow"
		else:
			self.array.append(value)
			self.set_top()
			self.size += 1
			self.pprint()

	def pop(self):
		if self.size == 0:
			print "Stack Underflow"
		else:	
			print "Removing the item " + str(self.top)
			self.array.pop()
			self.set_top()
			self.size -= 1
			self.pprint()

	def pprint(self):                         # could have used self.array.reverse() for the same thing
		if 	self.is_empty == True:
			print "Stack Empty"
		else:	
			print "-------------> Top <------------"
			i= 0
			while i < len(self.array):
				i+=1
				print "|              ^"	+ str(self.array[i*-1]) + "             |"
			print "================================"



 ## Sample Implementation

# >>> s=Stack(3,[31,32,89])
# -------------> Top <------------
# |              ^89             |
# |              ^32             |
# |              ^31             |
# ================================
# >>> 

# ................. Removing Some mid Part

# >>> s.pop()
# Removing the item 31
# -------------> Top <------------
# ================================
# >>> s.pop()
# Stack Underflow
# >>> 
# >>> 
# >>> s.pop()
# Stack Underflow
# >>> 
# >>> 
# >>> s.push(21)
# -------------> Top <------------
# |              ^21             |
# ================================
# >>> s.push(24)
# -------------> Top <------------
# |              ^24             |
# |              ^21             |
# ================================
# >>> s.push(29)
# -------------> Top <------------
# |              ^29             |
# |              ^24             |
# |              ^21             |
# ================================
# >>> s.push(32)
# Stack Overflow

# Stack Overflow
