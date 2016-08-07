# Given a list of strings which might be anagrams of each other,
# print each set of anagrams separately.

max_length = 32767 # max length possible for a string
base_sum = max_length * ord('z')


def create_hash(s):
    if not s:
        raise AttributeError("Can't be null or empty string")

    ord_sum = 0
    for i in s:
        ord_sum += ord(i)

    return ord_sum % base_sum


def store_anagrams(l):
    if not l:
        raise AttributeError("list of strings can't be empty")

    hashmap = dict()
    for i in l:
        hash = create_hash(i)
        if hash not in hashmap:
            hashmap[hash] = [i]
        else:
            hashmap[hash].append(i)

    return hashmap


if __name__ == "__main__":
    N = int(raw_input())
    strings = []

    for i in range(N):
        strings.append(raw_input())

    map = store_anagrams(strings)
    for k, v in map.items():
        print v
