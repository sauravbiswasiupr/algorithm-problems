##testing some functionalities on BST

from BSTLib import *

if __name__ == "__main__":
	arr = map(lambda x: int(x), raw_input().split(" "))

	tree = BST(arr)

	root = tree.root

	print "Inorder Traversal..."
	tree.inOrderTraversal(root)
	print "PreOrderTraversal..."
	tree.preOrderTraversal(root)
	print "PostOrderTraversal..."
	tree.postOrderTraversal(root)
