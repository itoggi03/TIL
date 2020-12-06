# SWEA_1949 등산로 조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE

import sys
sys.stdin = open("sample_input.txt", "r")

# 배열 인덱스 넘는지 체크해주는 함수
def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

# 가장 긴 등산로를 찾아주는 dfs
def dfs(x, y, cut, length, val):
    global max_len
    visited[x][y] = 1
    if length > max_len:
        max_len = length
    for d in range(4):
        nx = x + dr[d]
        ny = y + dc[d]
        if check(nx, ny) and not visited[nx][ny]:
            # 현재 위치보다 높이가 낮으면
            if val > mountain[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, cut, length+1, mountain[nx][ny])
                visited[nx][ny] = 0

            # 현재 위치보다 높이가 높고, 공사한적이 없으면
            elif not cut and val <= mountain[nx][ny]:
                if mountain[nx][ny] - K < val:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cut+1, length+1, val-1)
                    visited[nx][ny] = 0


for tc in range(1, int(input())+1):
    # N: 지도 한 변의 길이, K:최대 공사 가능 깊이
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    # 시작 지점 찾기(가장 높은 곳)
    start = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] >= start:
                start = mountain[i][j]

    # 높은 지점들에서 각각 dfs
    cut = 0
    max_len = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == start:
                visited = [[0] * N for _ in range(N)]
                dfs(i, j, 0, 0, start)


    print('#{} {}'.format(tc, max_len+1))