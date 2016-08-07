from Queue import Queue


class BoardEntry:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance # distance is distance from origin (0, 0)


def min_moves_to_win(moves, N):
    visited = set()
    q = Queue()
    boardEntry = BoardEntry(0, 0)
    q.put(boardEntry)
    visited.add(0)
    entry_now = None
    while not q.empty():
        entry_now = q.get()
        v = entry_now.vertex

        if v == N-1:
            break

        j = v + 1
        while (j <= v + 6) and (j < N):
            if j not in visited:
                dist = entry_now.distance + 1
                visited.add(j)

                if moves[j] != -1:
                    vertex = moves[j]
                else:
                    vertex = j

                entry = BoardEntry(vertex, dist)
                q.put(entry)

            j += 1

    return entry_now.distance


if __name__ == "__main__":
    N = 30
    moves = []
    for i in range(N):
        moves.append(-1)

    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print min_moves_to_win(moves, N)


