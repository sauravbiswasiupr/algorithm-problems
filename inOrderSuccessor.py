## aLgo to find inorder successor of a node 
## inputs to the function are root node and the node 
## for which we find the successor

from BSTLib import *

if __name__ == "__main__":
	a = map(lambda x: int(x), raw_input().split(" "))
	root = None

	bst = BST()
	for d in a:
		root = bst.insertNode(root, d)

	print "Initial tree..."
	bst.inOrderTraversal(root)

	node = root.left.right.right

	print "Node for which we find successor is ...", node.data
	print "Successor is: ", bst.inOrderSuccessor(root, node)