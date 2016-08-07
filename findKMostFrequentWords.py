# Find k most frequent words given a list of words to look for.

import heapq


def find_k_most_frequent_words(words, k):
    if not words or not isinstance(words, list):
        raise AttributeError("Need a valid list of words")

    heap = []
    word_map = dict()

    for word in words:
        if not word in word_map:
            word_map[word] = 1
        else:
            word_map[word] += 1

    keys = word_map.keys()
    if k >= len(keys):
        keys.sort()
        return keys

    else:
        # Number of words to look for is less than length of array
        # Create a min heap and store the first k elements in the heap
        for i in xrange(k):
            key = keys[i]
            heapq.heappush(heap, (word_map[key], key))
            heapq.heapify(heap)

        # Now for the rest of the keys, see if the root of the min heap has word count
        # less than the current key, if so we need to pop the root, insert the key
        # and do the min heapify operation by default
        for i in range(k, len(keys)):
            count = heap[0][0]
            key = keys[i]
            if word_map[key] > count:
                popped = heapq.heappop(heap)
                heapq.heappush(heap, (word_map[key], key))
                heapq.heapify(heap)

        return heap

if __name__ == "__main__":
    words = raw_input().split(" ")
    k = int(raw_input())

    print "K most frequent words: ", find_k_most_frequent_words(words, k)
