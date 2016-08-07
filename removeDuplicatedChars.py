## Given a string s, remove all duplicated characters from it
## maintaining the order of the characters

def removeDuplicated(s):
	dictChars = {}
	newS = ""

	for char in s:
		val = dictChars.get(char)
		if val is None:
			newS = newS + char
			dictChars[char] = True

		if val is True:
			continue


	return newS

def removeDuplicatesInPlace(s):
	##Strings are immutable so we must use a list
	l = [c for c in s]
	print l
	r = i = 0
	dict = {}

	for el in l:
		if dict.get(el) is None:
			dict[el] = True
			l[r] = l[i]
			r = r + 1

		i = i + 1


	return "".join(l[:r])



if __name__ == "__main__":
	s = raw_input()
	print removeDuplicatesInPlace(s)
