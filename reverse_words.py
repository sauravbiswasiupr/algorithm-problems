# Given a sentence reverse the order of the words, without reversing the character order in each individual word.
# E.g: I like cats --> cats like I


def reverse_words_pythonic(words):
    if not words:
        return None

    l = words.split(" ")
    return " ".join(reversed(l))


def reverse_list(l, start, end):
    while start < end:
        temp = l[start]
        l[start] = l[end]
        l[end] = temp
        start += 1
        end -= 1


def reverse_in_place(s):
    if not s:
        return None

    # First pass, reverse complete string.
    # Second pass, reverse each individual word.

    l = [j for j in s]
    N = len(l)
    reverse_list(l, 0, N-1)

    start = 0
    end = 0
    print l
    while end < N:
        if l[end] == " ":
            reverse_list(l, start, end-1)
            start = end + 1
        end += 1

    reverse_list(l, start, end-1)
    print "".join(l)

if __name__ == "__main__":
    s = raw_input()
    print "Reversed in the pythonic sense:", reverse_words_pythonic(s)
    print "Reverse in place: "
    reverse_in_place(s)
