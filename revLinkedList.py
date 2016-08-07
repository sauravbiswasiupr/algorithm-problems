# Algorithm to reverse a linked list
# E.g 1->2->3->4 would become 4->3->2->1

from linkedListLib import *


def reverseLinkedList(prev, node):
    if node is None: return prev

    copy = node.next
    node.next = prev
    prev = node
    return reverseLinkedList(prev, copy)


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    head = createLinkedList(arr)
    print "Reversing ..."
    head_reversed = reverseLinkedList(None, head)
    print "Reversed stuff: ", printLinkedList(head_reversed)
