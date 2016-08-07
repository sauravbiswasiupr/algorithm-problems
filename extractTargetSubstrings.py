#Extract all the the combinations of a target substring that appear in a source string. I.e: target: 
#"abc", source:"abcdefgbcahijkacb12df", solution: {abc, bca, acb}

def hash_function(s):
	if s == None or len(s) == 0:
		return 0

	hash = 0
	for c in s:
		hash = hash + 26 * (ord(c) - ord('a'))

	return hash


def findAllSubstrings(s,p):
	if s == None or len(s) == 0:
		return []

	if p == None:
		return []

	if len(p) == 0:
		return []

	hash = hash_function(p)
	n = len(p)
	N = len(s)

	results = set()

	for i in range(N - 2):
		substring = s[i:i+3]

		if hash_function(substring) == hash:
			results.add(substring)

	return list(results)

if __name__ == '__main__':
	s = raw_input()
	p = raw_input()

	print "Occurrences: ", findAllSubstrings(s, p)
