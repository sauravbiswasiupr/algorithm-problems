##Given an linked list
##reverse alternate nodes and append them to end of list. 
#Extra allowed space is O(1) 

from linkedListLib import *

def createList(head, node):
	node.next = head
	head = node
	return head

def spliceList(head):
	n = 0

	headOddList = head
	while head is not None:
		n = n + 1
		head = head.next


	i = 1

	headEvenList = None
	current = headOddList
	prev = None
	while i <= n:
		curr = current
		
		if i % 2 == 0:
			prev.next = current.next
			current = current.next
			headEvenList = createList(headEvenList,curr)
			
		else:
			prev = current
			current = current.next

		i = i + 1

	prev.next = headEvenList
	return headOddList

if __name__ == "__main__":
	arr = map(lambda x: int(x), raw_input().split(" "))
	headMain = createLinkedList(arr)
	head = headMain
	print "Original list: "
	printLinkedList(headMain)
	headNew = spliceList(head)
	print
	print "New swapped list..."
	printLinkedList(headNew)

