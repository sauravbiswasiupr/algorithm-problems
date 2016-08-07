# Given a string, remove all duplicate characters from it.
# Bonus points: Do it in place


def remove_dups_from_string(s):
    # Uses a hashmap so space complexity is O(n)
    if not s:
        return s

    if len(s) == 1:
        return s

    hashmap = dict()
    l = [i for i in s]
    i = 0
    j = 0

    for c in l:
        if not c in hashmap:
            hashmap[c] = True
            l[i] = l[j]
            i += 1
            j += 1
        else:
            j += 1

    return "".join(l[:i])


def remove_dups_without_extra_space(s):
    if not s or len(s) == 1:
        return s
    pass


if __name__ == "__main__":
    s = raw_input()
    print remove_dups_from_string(s)