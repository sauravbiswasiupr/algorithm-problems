def find_max_index_difference(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return None

    hashmap = dict()
    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = [0, i]
        else:
            values = hashmap[arr[i]]
            min_index_till_now = values[1]
            max_diff_index = max(values[0], abs(i-min_index_till_now))
            min_index_new = min(min_index_till_now, i)
            hashmap[arr[i]][0] = max_diff_index
            hashmap[arr[i]][1] = min_index_new

    maximum = 0
    for k, v in hashmap.items():
        if v[0] > maximum:
            maximum = v[0]

    return maximum


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    print "Max diff index is: ", find_max_index_difference(arr)