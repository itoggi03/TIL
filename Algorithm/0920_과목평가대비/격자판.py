# import sys
# sys.stdin = open("sample_input.txt")

def check(i, j):
    if i >= 0 and i < 4 and j >= 0 and j < 4:
        return True
    else:
        return False

def bfs(x, y):
    cnt = 0
    Q.append([x, y, arr[x][y], cnt])
    while Q:
        X, Y, val, c = Q.pop(0)
        if c ==6:
            result.append(val)
            continue
        for d in range(4):
            newX = X + dx[d]
            newY = Y + dy[d]
            if check(newX, newY):
                Q.append([newX, newY, val + arr[newX][newY], c+1])

T = int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = []
    Q = []



    for i in range(4):
        for j in range(4):
            bfs(i, j)

    # print(result)
    aws = len(set(result))
    print('#{} {}'.format(tc, aws))