# Given an array of size n, select the minimum k elements from this array.
import heapq


def find_min_k_elements(arr, k):
    if not arr:
        raise AttributeError("Can't have an empty array")

    if len(arr) <= k:
        arr.sort()
        return arr

    # k is less than N
    heap = []

    for i in range(k):
        heap.append(arr[i])

    # create a max heap
    heapq._heapify_max(heap)

    for i in range(k, len(arr)):
        element = arr[i]
        if element < heap[0]:
            heapq.heappop(heap)
            heap.append(element)
            heapq._heapify_max(heap)

    return heap


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    K = int(raw_input("K: "))
    print find_min_k_elements(arr, K)
