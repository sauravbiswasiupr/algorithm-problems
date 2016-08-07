# Algorithm to check if a given string can be converted to a palindrome.
# A string can be converted to a palindrome if it contains at most one character that
# occurs odd number of times and all other characters occur even number of times


def checkIfStringIsPalindrome(s):
	if s == None:
		return False

	n = len(s)
	if n == 0:
		return True ## empty string is palindrome

	hashmap = {}

	for c in s:
		if hashmap.get(c) == None:
			hashmap[c] = 1
		else:
			hashmap[c] = hashmap[c] + 1


	oddcount = 0
	oddchar = None

	for key in hashmap.keys():
		if hashmap[key] % 2 != 0:
			oddcount = oddcount  + 1
			oddchar = key

	if oddcount == 0 or oddcount == 1:
		front  = []; back = []
		for key in hashmap.keys():
			if key != oddchar:
				front.append(key); back.append(key)

		newS = ""
		
		for i in front:
			newS = newS + i
		if oddchar != None:
			newS = newS + oddchar
		for i  in reversed(back):
			newS = newS + i
		
		return True, newS

	else:
		return False, None

if __name__ == '__main__':
	s = raw_input()
	print "Can be palindrome: ", checkIfStringIsPalindrome(s)