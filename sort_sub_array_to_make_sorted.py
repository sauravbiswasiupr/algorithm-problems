# Given a partially sorted array, devise an algo to find the minimum number of contiguous elements
# that need to be sorted to make the array completely sorted.


def min_subsegment_to_sort(arr):
    if not arr:
        return 0

    if len(arr) == 1:
        return 0

    copy = [i for i in arr]
    copy.sort()

    i = 0
    count = 0
    found = False
    while i < len(arr):
        if copy[i] != arr[i]:
            print "Unequal value: ", copy[i]
            found = True

        i += 1
        if found:
            count += 1
    return count


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    print min_subsegment_to_sort(arr)