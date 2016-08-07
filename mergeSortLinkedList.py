## Algorithm to merge two sorted linkedlists 
## e.g 1->3->7 and 2->4->10 : 1->2->3->4->7->10

from linkedListLib import *

def splitLists(head):
	if head == None or head.next == None:
		head1 = head; head2 = None
		return head1, head2

	slow = head; fast = head.next

	while fast != None:
		fast = fast.next

		if fast != None:
			slow = slow.next
			fast = fast.next

	head1 = head; head2 = slow.next
	slow.next = None # important step to end the first list

	return head1, head2

def mergeSortLinkedLists(head):
	if head == None or head.next == None:
		return head

	head1, head2 = splitLists(head)
	
	head1_new = mergeSortLinkedLists(head1)
	head2_new = mergeSortLinkedLists(head2)
	newhead = mergeLinkedLists(head1_new, head2_new)

	return newhead

def mergeLinkedLists(head1, head2):
	result = None
	if head1 == None:
		return head2

	if head2 == None:
		return head1

	if head1.data <= head2.data:
		result = head1
		result.next = mergeLinkedLists(head1.next, head2)

	else:
		result = head2
		result.next = mergeLinkedLists(head1, head2.next)

	return result

if __name__ == '__main__':
	a = map(lambda x: int(x), raw_input().split(" "))
	#a2 = map(lambda x: int(x), raw_input().split(" "))

	head = createLinkedList(a)
	#head2 = createLinkedList(a2)

	newhead = mergeSortLinkedLists(head)
	print "Sorted linkedlist ..."
	printLinkedList(newhead)