## Algorithm to remove duplicates from a linked list
## method 1: use a dict to store the values
from linkedListLib import *

def removeDupsFromLinkedList(head):
	dict = {}
	
	prev = None
	node = head

	while node != None:
		if dict.get(node.data) is None:
			dict[node.data] = True
			prev = node
			node = node.next
		else:
			prev.next = node.next
			node = node.next


	return head


if __name__ == "__main__":
	a = raw_input().split(" ")
	head = createLinkedList(a)
	headnew = removeDupsFromLinkedList(head)

	printLinkedList(headnew)

