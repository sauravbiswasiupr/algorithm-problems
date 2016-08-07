## program to test one by one insertion of data in linkedlist

from linkedListLib import *

def insertAllElements(a):
	a.reverse()
	head = None
	for i in a:
		head = insertOneByOne(head, i)

	return head

if __name__ == '__main__':
	a = map(lambda x: int(x), raw_input().split(" "))
	head = insertAllElements(a)

	printLinkedList(head)