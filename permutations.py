## Given a string, find all permutations that can be generated from that string
## e.g abc --> abc, acb, bac, bca, cab, cba


def permute(l, low, high, results = []):
	if low == high:
		results.append("".join(l))
	else:
		for i in range(low, high + 1):
			temp = l[i]
			l[i] = l[low]
			l[low] = temp

			permute(l, low + 1, high, results)

			temp = l[i]
			l[i] = l[low]
			l[low] = temp

if __name__ == '__main__':
	s = raw_input()
	l = [i for i in s]
	results = []
	permute(l, 0, len(s) - 1, results)

	print "Permutations are: ", results
