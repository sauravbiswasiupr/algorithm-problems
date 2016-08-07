## design an algorithm for a custom regex matcher
## * matches 0 or more of preceding chars 
## . matches exactly one char
## matcher(s, p) where s is input string and p is pattern

## matcher("aab", "a*b") --> True
## matcher("abcab", "a*b*c*b") --> True

def patternMatcher(s, p):
	print "S now: ", s
	print "P now: ", p
	if len(s) == 0 and len(p) == 0:
		return True

	if p == None:
		return True

	if len(p) == 0:
		return True

	if p == "*" and s != None:
		return True

	if p == "." and len(s) == 1:
		return True

	if p == s:
		return True

	first = p[0]

	if first != "*" and first != ".":
		if first == s[0]:
			return patternMatcher(s[1:], p[1:])
		
		elif len(p) > 1 and p[1] == "*":
			return patternMatcher(s[1:], p[2:])

		else:
			return False


	elif first == ".":
		return patternMatcher(s[1:], p[1:])

	elif first == "*" and len(p) > 1:
		second = p[1]
		i = 0
        
		while i < len(s):
			if s[i] != second:
				i = i + 1
			else:
				break

		if i == len(s):
			print "i = len(s)"
			return False
		else:
			return patternMatcher(s[i+1:], p[2:])
	else:
		return False

if __name__ == '__main__':
	s = raw_input()
	p = raw_input()

	print "Pattern present in String: ", patternMatcher(s, p)