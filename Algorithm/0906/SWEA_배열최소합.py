import sys
sys.stdin = open("sample_input2.txt", "r")

def findmin(x):
    global tmp, minV
    if tmp > minV:
        return
    elif x == N:
        if tmp < minV:
            minV = tmp
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            tmp += arr[x][i]
            findmin(x+1)
            visited[i] = 0
            tmp -= arr[x][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = 0
    minV = 100000
    visited = [0]* N
    findmin(0)

    print('#{} {}'.format(tc, minV))

