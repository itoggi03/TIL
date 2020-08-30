# BOJ1012: 유기농 배추
# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt", "r")

# 인덱스가 보드의 범위를 넘어가는지 확인해주는 함수
def check(i, j):
    if i >= 0 and i < N and j >= 0 and j < M:
        return True
    else:
        return False

# 인접해 있는 유기농 배추 체크하는 함수
def cabbage(x, y):
    visited[x][y] = 1   # 방문했을 경우 1로 바꿈
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        # 인접한 곳이 1일 경우 그곳에서 다시 함수 호출
        if check(newX, newY) and visited[newX][newY] != 1 and BRD[newX][newY] == 1:
            cabbage(newX, newY)

T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    BRD = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        BRD[Y][X] = 1

    cnt = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0 and BRD[x][y] == 1:
                cabbage(x, y)
                cnt += 1

    print(cnt)