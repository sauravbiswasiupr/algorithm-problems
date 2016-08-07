# Algorithm to tokenize a sentence into words and return count for each words

def tokenizeSimple(sentence):
	words = sentence.split(" ")
	hashmap = {}

	for word in words:
		if hashmap.get(word) is None:
			hashmap[word] = 1
		else:
			hashmap[word] = hashmap[word] + 1


	wordCount = []

	for key in hashmap.keys():
		wordCount.append((key, hashmap[key]))

	return wordCount

def tokenize(sentence):
	start = 0
	end = 0
	n = len(sentence)
	hashmap = {}

	while end < n:
		if sentence[end] == " ":
			word = sentence[start:end]
			if hashmap.get(word) is None:
				hashmap[word] = 1
			else:
				hashmap[word] = hashmap[word] + 1

			start = end + 1
		end = end + 1

	word = sentence[start:end]
	if hashmap.get(word) is None:
		hashmap[word] = 1
	else:
		hashmap[word] = hashmap[word] + 1


	wordCount = []
	for key in hashmap.keys():
		wordCount.append((key, hashmap[key]))

	return wordCount

if __name__ == "__main__":
	s = raw_input()
	print "Normal tokenize: ", tokenize(s)
	print "Lib tokenize: ", tokenizeSimple(s)



 

