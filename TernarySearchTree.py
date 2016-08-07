# A Basic Ternary Search tree implementation
# It allows insertion, search and nearest word lookups.

class Node:
	def __init__(self, c):
		self.char = c
		self.left = None
		self.right = None
		self.equal = None
		self.end = False


class TernarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, word, node):
		char = word[0]

		if node == None:
			node = Node(char)

		if ord(char) < ord(node.char):
			node.left = self.insert(word, node.left)

		if ord(char) > ord(node.char):
			node.right = self.insert(word, node.right)

		if word[1:]:
			node.equal = self.insert(word[1:], node.equal)
		else:
			node.end = True
		
		return node
			
if __name__ == '__main__':
	word = "chicken"
	tst = TernarySearchTree()
	root = tst.insert(word, tst.root)
	root = tst.insert("bug", root)

	node = root
	print node.char

	while root != None:
		print root.char,
		root = root.equal


