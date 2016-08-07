# Given a dictionary of words, write a function that takes two words as input and returns the minimum number of
# transformations (intermediate words) to reach from the source to destination word. At each transform step, only
# one character can be edited or changed at that time. At each step the generated intermediate word must be a valid
# word in the provided dictionary
from Queue import Queue


def transform(word1, word2, dictionary):
    if not all([word1, word2]):
        return False

    transformation_list = []
    word_queue = Queue()
    visited = set()
    backtrack_map = {}

    word_queue.put(word1)
    visited.add(word1)

    while not word_queue.empty():
        word = word_queue.get()

        for w in generate_one_edit_words(word):
            if w == word2:
                transformation_list.append(w)
                while word is not None:
                    transformation_list.append(word)
                    word = backtrack_map.get(word)
                return transformation_list[::-1]

            if w in dictionary:
                if w not in visited:
                    visited.add(w)
                    backtrack_map[w] = word
                    word_queue.put(w)

    return []


def generate_one_edit_words(s):
    wordset = set()
    word_arr = [i for i in s]
    n = len(word_arr)

    for i in range(n):
        for j in range(ord('a'), ord('z') + 1):
            if chr(j) != word_arr[i]:
                temp = word_arr[i]
                word_arr[i] = chr(j)
                wordset.add("".join(word_arr))
                word_arr[i] = temp  # put back

    return wordset


if __name__ == "__main__":
    word1 = raw_input()
    word2 = raw_input()
    dict_words = raw_input().split(" ")
    dict_words = set(dict_words)

    print transform(word1, word2, dict_words)
