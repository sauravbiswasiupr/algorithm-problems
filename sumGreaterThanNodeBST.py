## Given a BST modify it such that every node value is replaced
## by the sum of all node (values) greater than it + its own value

from BSTLib import *

def modifyBST(root, sum=[0]):
	if root == None:
		return

	modifyBST(root.right, sum)
	sum[0] = sum[0] + root.data
	root.data = sum[0]
	modifyBST(root.left, sum)

if __name__ == '__main__':
	a = map(lambda x: int(x), raw_input().split(" "))
	bst = BST(a)
	print "Tree initially ..."
	bst.inOrderTraversal(bst.root)
	modifyBST(bst.root, [0])
	print "After modification ..."
	bst.inOrderTraversal(bst.root)



