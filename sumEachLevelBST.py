# Given a BST find sum of nodes at each level
# The classical case of level order traversal.

from BSTLib import *
from Queue import Queue

def findLevelOrderSumBST(root):
	if root == None:
		return root

	results = []
	level = 0; levelsum = 0

	q = Queue()
	q.put((root, level))

	while not q.empty():
		node, currlevel = q.get()

		leftchild = node.left
		rightchild = node.right

		if leftchild != None:
			q.put((leftchild, currlevel + 1))

		if rightchild != None:
			q.put((rightchild, currlevel + 1))

		if currlevel == level:
			levelsum = levelsum + node.data

		else:
			results.append(levelsum)
			levelsum = node.data

			level = currlevel

	results.append(levelsum)
	return results

if __name__ == "__main__":
	a = map(lambda x: int(x), raw_input().split(" "))
	bst = BST(a)
	print "root is: ", bst.root.data
	results = findLevelOrderSumBST(bst.root)
	print "Level order sums: ", results






