def removeDuplicatesFromArray(arr):
	if arr == None:
		return 0

	n = len(arr)
	if n == 1:
		return n

	l = r = 0;
	dict = {}

	for el in arr:
		if dict.get(el) == None:
			dict[el] = True
			arr[r] = arr[l]
			r = r + 1

		l = l + 1

	arr = arr[:r]
	return r

if __name__ == '__main__':
	arr = map(lambda x: int(x), raw_input().split(" "))
	print "Distinct elements: ", removeDuplicatesFromArray(arr)

