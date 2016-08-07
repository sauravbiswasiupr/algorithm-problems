# Given a text T[0...n-1] and patter p[0...m-1], find all the indexes where the pattern matches the string


def naive_pattern_matcher(text, pat):
    if not pat:
        return True
    if not text:
        return False

    N = len(text)
    M = len(pat)

    for i in range(N-M+1):
        for j in range(M):
            if pat[j] != text[i+j]:
                break

        if j == M-1:
            print "Pattern found at index {}".format(i)


if __name__ == "__main__":
    text = raw_input()
    p = raw_input()
    naive_pattern_matcher(text, p)