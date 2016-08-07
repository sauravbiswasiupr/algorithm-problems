## A very basic Trie implementation to insert a word and search a word

## each node will store the letter for that node
## the links as a dict to all other nodes and a variable that 
## indicates if this is an ending word

class TrieNode:
	def __init__(self, char):
		self.char = char
		self.links = {}
		self.end = False


class Trie:
	def __init__(self):
		self.root = TrieNode("\0")

	def insert(self, word):
		current = self.root

		for c in word:
			if current.links.get(c) is None:
				current.links[c] = TrieNode(c)

			current = current.links[c]
			#if current.end is True:
			#	current.end = False

		current.end = True

	def search(self, word):
		current = self.root
		found = False

		for c in word:
			if current.links.get(c) is None:
				return found

			current = current.links[c]


		if current is not None and current.end is True:
			found = True

		return found

	def DFS(self, node, s, results):
		if node.end == True:
			print "Autocomplete string: ", s
			results.add(s)

		for key in node.links.keys():
			self.DFS(node.links[key], s + key, results)
		

	def autocomplete(self, word):
		current  = self.root
		results = set()

		for char in word:
			if current.links.get(char) is None:
				return list(results)
			current = current.links.get(char)

		self.DFS(current, "", results)
		res = [word + i for i in list((results))]
		return res



if __name__ == "__main__":
	tree = Trie()
	print "Enter some words to store in the trie..."
	words = raw_input().split(" ")

	for word in words:
		tree.insert(word)


	print "Enter a word to search ..."
	word = raw_input()

	print tree.search(word)
	print "Enter a word to autocomplete: ",
	s = raw_input()
	print tree.autocomplete(s)

