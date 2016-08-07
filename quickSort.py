# recursive version of quicksort 


def partition(arr, l, h):
	x = arr[h]
	i = l-1

	for j in xrange(l, h):
		if arr[j] < x:
			i = i + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

	temp = arr[i+1]
	arr[i+1] = x
	arr[h] = temp

	return i+1


def quickSort(arr, l, h):
	if l < h:
		p = partition(arr, l, h)
		quickSort(arr, l, p-1)
		quickSort(arr, p+1, h)

if __name__ == '__main__':
	arr = map(lambda x: int(x), raw_input().split(" "))
	print "Sorted array: "
	quickSort(arr, 0, len(arr)-1)
	print arr
