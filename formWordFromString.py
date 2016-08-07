## Given a word w and random string s, return True if you can form the word
## from the string, otherwise False
## e.g f('apple', 'sxryppaelwb') --> True 

def wordExists(word, s):
	if s == None or word is None:
		return False

	if word == "":
		return True
	
	hashmap = {}
	for char in s:
		if hashmap.get(char) is None:
			hashmap[char] = 1
		else:
			hashmap[char] = hashmap[char] + 1

	for c in word:
		if hashmap.get(c) is None:
			return False
		else:
			hashmap[c] = hashmap[c] - 1

	exists = True
	for key in hashmap.keys():
		if hashmap[key] < 0:
			exists = False
			break

	return exists

if __name__ == "__main__":
	word, s = raw_input().split(" ")
	print "Exists: ", wordExists(word, s)