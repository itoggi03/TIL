import sys
sys.stdin = open("input2.txt", "r")


# x, y좌표가 배열의 인덱스를 넘는지 확인해주는 함수
def check(x, y):
    if x >= 0 and y >= 0 and x < N and y < N:
        return True
    else:
        return False


# 인접한 8곳에 지뢰가 1개 이상 있으면 1을 return, 아니면 0을 return하는 함수
def cnt(x, y):
    cx, cy = x, y
    for dir in range(8):
        nx, ny = cx + dr[dir], cy + dc[dir]
        if check(nx, ny) and arr[nx][ny] == '*':
            return 1
    return 0


# new_list의 값이 0인 곳 주변 8방향을 탐색하는 함수.
def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1

    while q:
        cx, cy = q.pop(0)
        # print(cx, cy)
        for d in range(8):
            nx = cx + dr[d]
            ny = cy + dc[d]
            if check(nx, ny) and not visited[nx][ny]:
                # visited를 1로 만들어주고,
                visited[nx][ny] = 1
                # new_list의 값이 0이면 q에 append
                if new_list[nx][ny] == 0:
                    q.append((nx, ny))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 왼쪽 대각선 위에서부터 시계방향으로 한바퀴
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]

    # 인접한 곳에 지뢰가 있는지를 표시하는 새로운 리스트 생성
    new_list = [['*'] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*':
                new_list[i][j] = cnt(i, j)

    ans = 0
    q = []
    visited = [[0] * N for _ in range(N)]
    # 주변에 지뢰가 없는 곳들에서(new_list에서 값이 0인 곳) bfs
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and new_list[i][j] == 0:
                bfs(i, j)
                ans += 1

    # visited의 값이 0이고 지뢰가 아닌 곳의 개수 카운트
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and new_list[i][j] != '*':
                ans += 1

    # 출력
    print('#{} {}'.format(tc, ans))


