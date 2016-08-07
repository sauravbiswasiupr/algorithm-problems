gold_set = set("abcdefghijklmnopqrstuvwxyz")


def checkIfPangram(s):
    if not s:
        return False

    if set([i for i in "".join(s.split(" "))]) == gold_set:
        return True
    else:
        return False


def construct_pangrams_from_list(l):
    if not l:
        raise AttributeError("Empty list")

    s = ""
    for i in l:
        if checkIfPangram(i):
            s += "1"
        else:
            s += "0"

    return s


if __name__ == "__main__":
    N = int(raw_input())
    l = []
    for i in range(N):
        l.append(raw_input())

    print construct_pangrams_from_list(l)
