from Queue import Queue

index = { "ang": set(["brad"]),
"brad": set(["ang", "jake"]),
"jake": set(["brad"]),
"gra":  set([])}


def findSep(actor1, actor2):
    visited = set()
    d = 0
    q = Queue()
    q.put(actor1)

    while not q.empty():
        actor = q.get()
        if actor == actor2:
            return d

        else:
            if actor not in visited:
                visited.add(actor)
                d += 1
                for el in index[actor]:
                    q.put(el)

    if not q.empty():
        return d
    else:
        return -1

if __name__ == "__main__":
    print findSep("ang", "gra")