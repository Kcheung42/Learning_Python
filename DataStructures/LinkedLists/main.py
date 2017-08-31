from linkedList import LinkedList

if __name__ == "__main__":
	print "Created list:"
	list = LinkedList([9,8,7,6,5,4,3,2,1,0])
	list.printList()

	print "length is:%d" %(list.getCount())

	print "Deleting Node 5..."
	list.delNode(5)
	list.printList()

	print "Appending Node 5..."
	list.append(5)
	list.printList()

	print "del node at pos Node 4..."
	list.delNodeAt(4)
	list.printList()

	print "is 6 in list:%r" %(list.isInList(6))
	print "is 11 in list:%r" %(list.isInList(11))
	print "3rd last is:%d" %list.getKthLast(3)
	list.printList()

	print "Deleting mid"
	list.delNodeMid()
	# list.delNodeMid2(list.head.next.next)
	list.printList()

	print "inserting at pos 2"
	list.insertNth(11,2)
	list.printList()

	print "appending 12"
	list.append(12)
	list.printList()

	print "deleting node 12"
	list.delNode(12)
	list.printList()

	print "appending 12"
	list.append(12)
	list.printList()

