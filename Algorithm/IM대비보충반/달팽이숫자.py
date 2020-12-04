import sys
sys.stdin = open("input_달팽이.txt", "r")

def solution():
    x, y = 0, 0
    newX, newY = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    num = 1

    for i in range(N*N):
        x, y = newX, newY
        arr[x][y] = num
        newX = x + dx[dir]
        newY = y + dy[dir]
        if newX < 0 or newX >= N or newY < 0 or newY >= N or arr[newX][newY] != 0:
            dir = (dir + 1) % 4
            newX = x + dx[dir]
            newY = y + dy[dir]

        num += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    # print(arr)

    solution()
    # print(arr)
    print('#{}'.format(tc))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()