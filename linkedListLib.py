class Node:
	def __init__(self, key):
		self.next = None
		self.data  = key


def createLinkedList(data):
	n = len(data)
	head = None

	for i in range(n-1, -1, -1):
		node = Node(data[i])
		node.next = head
		head = node

	return head

def printLinkedList(head):
	node = head
	while node != None:
		print str(node.data) + "-->",
		node = node.next

	print None

def insertOneByOne(head, data):
	newNode = Node(data)
	newNode.next = head
	head = newNode
	return head