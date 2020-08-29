# BOJ2667: 단지번호 붙이기
# https://www.acmicpc.net/problem/2667

import sys
sys.stdin = open("input.txt", "r")

# 인덱스가 보드의 범위를 넘어가는지 확인해주는 함수
def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

# 단지별로 같은 숫자로 바꿔주는 함수
# 해당 좌표의 상하좌우 방향을 보고 주변에 1인 곳이 있으면 그곳을 num으로 바꿔준 후 그 좌표에서 다시 complex 함수 호출
def complex(x, y):
    global num, cnt
    BRD[x][y] = num     # 해당 좌표의 값을 num으로 바꿈
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if check(newX, newY) and BRD[newX][newY] == 1:
            BRD[newX][newY] = num
            cnt += 1        # 바꾼 횟수 카운트(== 단지 내 집의 수)
            complex(newX, newY)

# 입력
N = int(input())
BRD = [list(map(int, input())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 2     # 단지 숫자를 2부터 시작(1부터 하면 체크하는데 헷갈리므로)
cnt = 0
hnum = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 1:
            complex(i, j)
            hnum.append(cnt)
            num += 1    # 단지 수 카운트
            cnt = 0

# 결과 출력
print(num - 2)      # num을 2부터 시작했으므로 단지 수는 num-2
hnum.sort()         # 단지 내 집 숫자 오름차순 정렬
for i in hnum:      # 한줄 씩 단지 별 집 숫자 출력
    print(i + 1)    # complex 함수에서 처음 시작 좌표를 바꿔준 것을 체크 안했으므로 +1 해서 출력
