# Implementation of binary search


def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low)/2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        if arr[mid] > key:
            high = mid - 1
    return -1


def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1

    mid = low + (high - low)/2
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return binary_search_recursive(arr, low, mid-1, key)

    if arr[mid] < key:
        return binary_search_recursive(arr, mid+1, high, key)

    return -1


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    key = int(raw_input())

    arr.sort()
    print "Binary search for {} and found at {}".format(key, binary_search(arr, 0, len(arr)-1, key))
    print "Binary search recursive for {} and found at {}".format(key, binary_search_recursive(arr, 0, len(arr)-1, key))
