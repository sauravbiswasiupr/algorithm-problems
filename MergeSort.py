def merge(a, l, m, r):
	a1 = a[l:m+1]
	a2 = a[m+1:r+1]
	print a1
	print a2
	n1 = len(a1)
	n2 = len(a2)

	i = j = 0;
	k = l

	while (i < n1) and (j < n2):
		if a1[i] <= a2[j]:
			a[k] = a1[i]
			i = i + 1
		else:
			a[k] = a2[j]
			j = j + 1

		k = k + 1

	while j < n2:
		a[k] = a2[j]
		k = k + 1
		j = j + 1

	while i  < n1:
		a[k] = a1[i]
		k = k + 1
		i = i + 1


def mergesort(a, l, r):
	m = (l + r)//2

	if l < r:
		mergesort(a, l, m)
		mergesort(a, m + 1, r)
		merge(a, l, m, r)
	

if __name__ == "__main__":
	inp = raw_input().split(" ")
	arr = [int(i) for i in inp]

	mergesort(arr, 0, len(arr) - 1)
	print "Sorted: ", arr