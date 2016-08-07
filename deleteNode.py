## algorithm to delete a node by data match in a BST

from BSTLib import *

if __name__ == "__main__":
	a = map(lambda x: int(x), raw_input().split(" "))

	val = int(raw_input())
	bst = BST(a)

	rootNew = bst.deleteNode(bst.root, val)
	print "Tree after deletion..."
	bst.inOrderTraversal(rootNew)
