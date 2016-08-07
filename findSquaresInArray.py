## Given 2 arrays, find all numbers in array 2 which are squares of existing numbers
## in array 1

def findSquaresInArray(a1, a2):
	n1 = len(a1)
	n2 = len(a2)

	if n2 == 0 or n1 == 0:
		return None

	hashmap = {}
	results = []

	for el in a1:
		hashmap[el] = True

	for el in a2:
		root = pow(el, 0.5)
		int_root = int(root)
		if root != int_root:
			continue

		pos_root = hashmap.get(int_root)
		neg_root = hashmap.get(-1*int_root)

		if pos_root == True:
			results.append(el)

		elif neg_root == True:
			results.append(el)

		else:
			continue

	return results

if __name__ == "__main__":
	a1 = map(lambda x: int(x), raw_input().split(" "))
	a2 = map(lambda x: int(x), raw_input().split(" "))

	results = findSquaresInArray(a1, a2)
	print results
