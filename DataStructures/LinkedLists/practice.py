class Node:
	def __init__(self, value=None, nextnode=None):
		self.value = value
		self.nextnode=None

class LinkedList:
	def __init__(self, values=None):
		self.head = None
		self.tail = None

	def append(self, value):
		if self.tail is None:
			self.tail = self.head = Node(value)
		else:
			self.tail.next = Node(value)
			self.tail = self.tail.next
	
	def appendMulti(self, values):
		for v in values:
			append(v)
	
	def push(self, value):
		if self.head is None:
			self.head = self.tail = Node(values)
		else:
			self.head = Node(values,self.head)
	
	def insertNth(self, value, pos):
		if(self.head is None):
			return
		cur = self.head
		if(pos == 0):
			cur.head = Node(value,cur.head)
		for i in range(pos-1):
			cur = cur.next
			if cur is None:
				return
		cur.next = Node(value, cur.next)
		if cur.next.next is None:
			self.tail = cur.next
