# Given a string segment it into all
# possible words separated by whitespace
# e.g applepie -> (Did you mean ?) apple pie
# Time complexity is O(N**2)


def segment_string_into_words(s, prefix_set, hashmap):
    if s is None:
        return None

    if s in prefix_set:
        return s
    if s in hashmap:
        return hashmap[s]

    n = len(s)
    for i in range(1, n):
        prefix = s[:i]
        if prefix in prefix_set:
            suffix = s[i:]
            segmented_suffix = segment_string_into_words(suffix, prefix_set, hashmap)

            if segmented_suffix:
                suggestion = prefix + " " + segmented_suffix
                hashmap[s] = suggestion
                return suggestion

    hashmap[s] = None
    return None


if __name__ == "__main__":
    string = raw_input()
    dictionary = set()
    dictionary.add("apple")
    dictionary.add("pie")
    dictionary.add("chicken")
    print segment_string_into_words(string, dictionary, {})

    print "Add some more words to dict.."
    dictionary = set()
    words = map(lambda x: x, raw_input().split(" "))
    map(lambda x: dictionary.add(x), words)
    s = raw_input("Enter a wrong string to be segmented: ")
    print segment_string_into_words(s, dictionary, {})

