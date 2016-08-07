# Given a string consisting of brackets such as {} or {{}} check
# if the string is balanced.


def checkBalancedParans(s):
	if s == None:
		return True

	n = len(s)
	if n == 1:
		return False

	stack = []

	stack.append(s[0])

	i = 1
	while stack and i < n:
		top = stack[-1]
		char = s[i]

		if top == "{" and char == "}":
			popped = stack.pop()

		elif top == "(" and char == ")":
			popped = stack.pop()

		elif top == "[" and char == "]":
			popped = stack.pop()

		else:
			stack.append(char)

		i = i + 1

	if stack:
		return False
	else:
		return True

if __name__ == '__main__':
	s = raw_input()
	print "Is balanced: ", checkBalancedParans(s)
