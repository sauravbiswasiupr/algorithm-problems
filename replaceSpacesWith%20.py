## Algorithm to replace a string's whitespaces with the characters %20
## e.g I am great --> I%20am%20great

def replaceSpaces(s):
	n = len(s)
	whitespaces = 0

	for c in s:
		if c == " ":
			whitespaces  = whitespaces + 1

	## extend the original list
	newLength = n + 2 * whitespaces
	newList = [None] * newLength

	i = n-1
	j = newLength - 1

	while i >= 0:
		if s[i] == " ":
			newList[j] = "0"
			newList[j - 1] = "2"
			newList[j - 2] = "%"
			j = j - 3

		else:
			newList[j] = s[i]
			j = j - 1
		i = i - 1

	return "".join(newList)


if __name__ == "__main__":
	s = raw_input()
	print "Replaced string is: ",
	print replaceSpaces(s)
