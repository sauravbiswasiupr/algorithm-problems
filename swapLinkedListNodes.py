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
		print node.data,
		node = node.next


def findPrevNodes(head, x, y):
	current_x = current_y = head;    prev_x = prev_y = None;

	while current_x and current_x.data != x:
		prev_x = current_x
		current_x = current_x.next

	while current_y and current_y.data != y:
		prev_y = current_y
		current_y = current_y.next


	if current_x is None or current_y is None:
		return None
	else:
		return current_x, prev_x, current_y, prev_y




def swapNodes(head, x, y):
	if head is None:
		return

	if x == y:
		return

	nodeList = findPrevNodes(head, x, y)
	if nodeList is not None:
		current_x, prev_x, current_y, prev_y = nodeList;
		if prev_x is None:
			head = current_y
			prev_y.next = current_x
			copy_current_x_next = current_x.next
			current_x.next = current_y.next
			current_y.next = copy_current_x_next

		elif prev_y is None:
			head = current_x
			prev_x.next = current_y
			copy_current_y_next = current_y.next
			current_y.next = current_x.next
			current_x.next = copy_current_y_next

		else:
			prev_x.next = current_y
			copy_current_x_next = current_x.next
			current_x.next = current_y.next
			prev_y.next = current_x
			current_y.next = copy_current_x_next

	return head




if __name__ == "__main__":
	a = map(lambda x: int(x), raw_input().split(" "))
	x = int(raw_input())
	y = int(raw_input())

	head = createLinkedList(a)
	printLinkedList(head)
	print "Swapping %d and %d" %(x, y)

	head = swapNodes(head, x, y)
	printLinkedList(head)