# check if there is a cycle in a linkedlist

from linkedListLib import *


def checkForCycle(head):
	if head is None:
		return False

	slow = head; fast = head

	while (slow != None and fast != None and fast.next != None):
		slow = slow.next
		fast = fast.next.next

		if slow == fast:
			return True

	return False

if __name__ == "__main__":
	root = Node(1)
	root.next = Node(2)
	root.next.next = Node(3)
	root.next.next.next = Node(4)
	root.next.next.next = Node(5)
	root.next.next.next.next = root.next

	print "Cycle present: ", checkForCycle(root)
