## Algorithm to separate odd and even numbers in an array such that
## odd are on one side and even are on another side

def separateEvenOdd(arr, l, h):
	if l == h:
		return arr

	x = arr[h]
	i = l - 1

	for j in range(l, h):
		if arr[j] % 2 == x %2 :
			i = i + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

	temp = arr[i+1]
	arr[i+1] = x
	arr[h] = temp

	return arr

if __name__ == "__main__":
	a = map(lambda x: int(x), raw_input().split(" "))
	newarr = separateEvenOdd(a, 0, len(a) - 1)
	print "New arr is: ", newarr