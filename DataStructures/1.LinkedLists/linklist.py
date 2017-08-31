class Node:
	def __init__(self,value=None, nextnode=None):
		self.value = value
		self.next = nextnode

class LinkedList:
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		if values is not None:
			self.appendMulti(values)

	# Insert a new node at the beginning
	def push(self, value):
		if(self.head is None):
			self.head = self.tail = Node(value)
		else:
			self.head = Node(value, self.head)

	# Insert new node at the end of a linked list
	def append(self, value):
		if self.tail is None:
			self.tail = self.head = Node(value)
		else:
			self.tail.next = Node(value)
			self.tail = self.tail.next

	# Insert a range of values (keep order)
	def appendMulti(self, values):
		for v in values:
			self.append(v)

	# Insert a new node after given prev node
	def insertAfter(self, prev_node, value):
		if prev_node is None:
			return
		prev_node.next = Node(value, prev_node.next)

	# Insert at Nth position
	def insertNth(self, data, pos):
		new_node = Node(data)
		if self.head is None:
			return
		if pos == 0:
			self.head = Node(data, self.head)
		else:
			cur = self.head
			for i in range(pos-1):
				cur = cur.next
				if cur is None:
					"pos does not exists"
					return
			cur.next = Node(data, cur.next)
			if cur.next.next is None:
				self.tail = cur.next

	# Delete a given key
	def delNode(self, key):
		cur = self.head
		if cur is not None:
			if cur.value == key:
				self.head = cur.next
				cur = None
				return
		while (cur is not None):
			if cur.value == key:
				break
			prev = cur
			cur = cur.next
		if cur is None:
			return
		prev.next = cur.next
		if cur == self.tail:
			self.tail = prev
		cur = None
	
	# Delete a key at a given position
	def delNodeAt(self, pos):
		cur = self.head
		if cur is None:
			return
		if pos == 0:
			self.head = cur.next
			cur = None
			return
		for i in range(pos-1):
			cur = cur.next
			if cur is None:
				break
		if cur is None or cur.next is None:
			return
		next = cur.next.next
		cur.next = None
		cur.next = next

	# Delete middle node
	def delNodeMid(self):
		if self.head is None:
			return;
		cur = self.head
		runner = self.head
		while runner.next:
			runner = runner.next.next
			prev = cur
			cur = cur.next
		prev.next = cur.next
		cur = None

	# Get length of list
	def getCountRec(self, node):
		if node is None:
			return (0)
		return( 1 + self.linkLen(node.next))

	# Get length of list Recursive
	def getCount(self):
		cur = self.head
		count = 0
		if cur is None:
			return (0)
		while(cur):
			cur = cur.next
			count += 1
		return(count)

	# Get first node with key
	def getNode(self, key):
		cur = self.head
		if cur is None:
			return (-1)
		while(cur):
			if cur.value == key:
				break
			cur = cur.next
		if cur is None:
			return (-1)
		return(cur)

	# Get Nth node
	def getNth(self, index):
		cur = self.head
		count = 0
		while (cur):
			if (count == index):
				return (cur.value)
			count += 1
		return (0);

	# Get Kth last node
	def getKthLast(self, k):
		runner = self.head
		cur = self.head
		if cur is None:
			return
		for i in range(k):
			if runner is None:
				return
			runner = runner.next
		while(runner):
			cur = cur.next
			runner = runner.next
		return (cur.value)

	# ? key is in list, Return True/False
	def isInList(self, key):
		cur = self.head
		while(cur):
			if cur.value == key:
				return True
			cur = cur.next
		return False

	# Utilitary function to print the node
	def printList(self):
		if self.head is None:
			print "List is empty"
			return;
		
		cur = self.head
		while(cur):
			print " %d" %(cur.value),
			cur = cur.next
		print ""
