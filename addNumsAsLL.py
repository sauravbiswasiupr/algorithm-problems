## Add two numbers represented as linkedlists
## e.g 3->1->5 + 5->9->2 = 8->0->8
from linkedListLib import *

def addLinkedLists(head1, head2):
	carry = 0

	node1 = head1; node2 = head2
	headNew = None
	prev = None
	n = 0

	while (node1 != None) or (node2 != None):
		if node1 is None:
			sum = node2.data + carry
		elif node2 is None:
			sum = node1.data + carry
		else:
			sum = node1.data + node2.data + carry

		carry = sum / 10
		sum = sum % 10

		node = Node(sum)
		if n == 0:
			headNew = node
			prev = node
		else:
			prev.next = node
			prev = prev.next

		if node1 is not None:
			node1 = node1.next

		if node2 is not None:
			node2 = node2.next

		n = n + 1

	if carry:
		prev.next = Node(carry)

	return headNew


if __name__ == "__main__":
	n1 = createLinkedList(map(lambda x: int(x), raw_input().split(" ")))
	n2 = createLinkedList(map(lambda x: int(x), raw_input().split(" ")))

	newList = addLinkedLists(n1, n2)
	print "Summed num: "
	printLinkedList(newList)





