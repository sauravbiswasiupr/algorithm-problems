# Some BST related helper functions


class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BST:
	def __init__(self, data=None):
		if data is not None:
		    data.sort()
		    self.root = self.createTree(data)
		else:
			self.root = None

	def createTree(self, data):
		n = len(data)
		if n == 0:
			return None

		if n == 1:
			return TreeNode(data[0])

		if n == 2:
			root = TreeNode(data[0])
			root.right = TreeNode(data[1])
			return root

		mid = n / 2
		root = TreeNode(data[mid])
		root.left = self.createTree(data[:mid])
		root.right = self.createTree(data[mid+1:])

		return root

	def inOrderTraversal(self, node):
		if node is None:
			return 

		self.inOrderTraversal(node.left)
		print node.data
		self.inOrderTraversal(node.right)

	def preOrderTraversal(self, node):
		if node is None:
			return
		print node.data
		self.preOrderTraversal(node.left)
		self.preOrderTraversal(node.right)

	def postOrderTraversal(self, node):
		if node is None:
			return 
		self.postOrderTraversal(node.left)
		self.postOrderTraversal(node.right)
		print node.data

	def insertNode(self, node, data):
		if node is None:
			return TreeNode(data)

		if data < node.data:
			if node.left is None:
				node.left = TreeNode(data)
			else:
				node.left = self.insertNode(node.left, data)
			
		else:
			if node.right is None:
				node.right = TreeNode(data)
			else:
				node.right = self.insertNode(node.right, data)
		
		return node
    
    ## Three cases
    ## 1. Both children of that node are null
    ## 2. One of them is null
    ## 3. Both children exist
	def deleteNode(self, node, data):
		if node is None:
			return node

		elif data < node.data:
			node.left = self.deleteNode(node.left, data)

		elif data > node.data:
			node.right = self.deleteNode(node.right, data)

		else:
			## node.data == data
			if node.left is None:
				temp = node.right
				node = temp
				return node

			if node.right is None:
				temp = node.left
				node = temp
				return node

			else:
				## both children exist
				## find inorder successor of node 
				## copy that value to this node and delete that
				## successor
				temp = node.right

				while temp.left != None:
					temp = temp.left

				node.data = temp.data
				node.right = self.deleteNode(node.right, node.data)

		return node

	def inOrderSuccessor(self, root, node):
		if root is None:
			return root

		if node is None:
			return node

		if node.right is not None:
			temp = node.right

			while temp.left is not None:
				temp = temp.left

			return temp.data

		## if node.right is None then we 
		## traverse from root down till we find the 
		## value just greater than node.data

		temp = root
		successor = None

		while temp is not None:
			if node.data < temp.data:
				successor = temp
				temp = temp.left
			elif node.data > temp.data:
				temp = temp.right
			else:
				break

		if successor is None:
			return None
		else:
			return successor.data



		






