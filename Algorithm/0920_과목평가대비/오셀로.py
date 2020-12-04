import sys
sys.stdin = open("sample_input(1).txt", "r")

def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

def change(x, y, c):
    cnt = 0
    for d in range(8):
        newX = x + dx[d]
        newY = y + dy[d]

        while check(newX,newY) and arr[newX][newY] == opp:
            # while check(newX,newY) and arr[newX][newY] == c:
            newX += dx[d]
            newY += dy[d]
        if check(newX, newY) and arr[newX][newY] == c:
            while x != newX or y != newY:
                newX -= dx[d]
                newY -= dy[d]
                arr[newX][newY] = c






T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N) for _ in range(N)]

    mid = N // 2
    arr[mid-1][mid-1] = 2
    arr[mid-1][mid] = 1
    arr[mid][mid-1] = 1
    arr[mid][mid] = 2
    # print(arr)
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, -1, -1, 1, 1]


    for i in range(M):
        x, y, dol = map(int, input().split())
        opp = dol % 2 + 1
        arr[x-1][y-1] = dol
        change(x-1, y-1, dol)

    cnt_w = 0
    cnt_b = 0
    for a in arr:
        cnt_b += a.count(1)
        cnt_w += a.count(2)

    print('#{} {} {}'.format(tc, cnt_b, cnt_w))

