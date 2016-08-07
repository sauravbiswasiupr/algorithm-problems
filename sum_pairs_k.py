# Find all pairs in an array that add up to a given number k


def find_pairs_with_given_sum(arr, k):
    if not arr:
        return []

    hashmap = dict()
    pairs = []

    for element in arr:
        other_element = k - element
        if other_element in hashmap:
            pairs.append((other_element, hashmap[other_element]))
            del hashmap[other_element]
        else:
            hashmap[element] = other_element

    return pairs


if __name__ == "__main__":
    arr = map(lambda x: int(x), raw_input().split(" "))
    k = int(raw_input())
    print "Pairs :", find_pairs_with_given_sum(arr, k)