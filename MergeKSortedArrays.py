## Algorithm to merge k sorted arrays ( each of size n ) into an array of size n*k
## Create a min heap of size k. Each heap element is the tuple (element, array_index, next_index)
## where array_index is the index of the array to which it belongs and next is the next index in the 
## array of that element to look at
import heapq
import sys

def mergeKSortedArrays(arrs):
	INT_MAX = sys.maxsize
	k = len(arrs)
	if k == 0:
		return None

	if k == 1:
		return arrs

	n = len(arrs[0])
	heap = []

	output = []

	for i in range(k):
		heapq.heappush(heap, (arrs[i][0], i, 1))

	for i in xrange(0, n*k):
		root = heapq.heappop(heap)
		output.append(root[0])

		next = root[2]
		arrindex = root[1]
		if next < n:
			newroot = (arrs[arrindex][next], arrindex, next + 1)
		else:
			newroot = (INT_MAX, arrindex, next + 1)

		heapq.heappush(heap, newroot)
		#heapq.heapify(heap)

	return output

if __name__ == '__main__':
	arrs = []

	N = int(raw_input())

	for i in xrange(N):
		inp_arr = map(lambda x: int(x), raw_input().split(" "))
		arrs.append(inp_arr)

	output = mergeKSortedArrays(arrs)
	print "New merged array: ", output
