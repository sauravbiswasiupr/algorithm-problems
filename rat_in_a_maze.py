# Rat in a maze problem. Given a Grid of size n*n, rat starts from (0,0) and has to reach (N-1, N-1). Find out if
# such a path exists and print that path. Note that there might be blockades in the maze (designated by 0).


def is_safe(maze, x, y, N):
    if x >= 0 and x <= N-1 and y >= 0 and y <= N-1 and maze[x][y] == 1:
        return True
    else:
        return False


def traverse_maze(maze, x, y, sol, N):
    print "Path now: ", sol
    if x == N-1 and y == N-1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y, N):
        sol[x][y] = 1
        if traverse_maze(maze, x+1, y, sol, N):
            return True
        if traverse_maze(maze, x, y+1, sol, N):
            return True

        sol[x][y] = 0  # backtrack since going either right or down didn't help rat reach.
        return False

    return False


def find_path(maze, N):
    sol = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        sol.append(row)

    if traverse_maze(maze, 0, 0, sol, N):
        print "Path exists...."
        print sol
    else:
        print "Path doesn't exist"


if __name__ == "__main__":
    N = int(raw_input())
    matrix = []
    for i in range(N):
        row = map(lambda x: int(x), raw_input().split())
        matrix.append(row)

    find_path(matrix, N)
