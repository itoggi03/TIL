import sys
sys.stdin = open("input.txt", "r")


def bfs(x, y):
    Q.append([x, y])
    visited[x][y] = 1
    while Q:
        tx, ty = Q.pop(0)
        if maze[tx][ty] == 3:
            return 1
        for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = tx + a, ty + b
            if visited[nx][ny] == 0 and maze[nx][ny] != 1:
                Q.append([nx, ny])
                visited[nx][ny] = 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    Q = []
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                result = bfs(i, j)

    print('#{} {}'.format(tc, result))