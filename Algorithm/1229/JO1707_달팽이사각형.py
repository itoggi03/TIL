# JO 1707 달팽이사각형
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=980&sca=2020

# 인덱스 넘었는지 확인해주는 함수
def check(r, c):
    if r >= 0 and r < n and c >= 0 and c < n:
        return True
    else:
        return False

# 규칙대로 숫자 넣어주는 함수
def snail(x, y):
    num = 1  # 넣을 숫자
    d = 0    # 방향 인덱스
    chk = 1  # 채운 횟수
    arr[x][y] = num
    num += 1

    while chk < cnt:    # 배열 크기(n*n)만큼만 while문 반복
        newX = x + dr[d]
        newY = y + dc[d]
        # 인덱스를 넘어가지 않고, 배열의 숫자가 0일 때만 숫자 채워넣기
        if check(newX, newY) and not arr[newX][newY]:
            arr[newX][newY] = num
            num += 1
            chk += 1
            x, y = newX, newY   # x, y 좌표 업데이트
        # 벽을 만났거나 이미 숫자가 채워진 곳 만날 경우 방향 바꾸기
        else:
            d = (d + 1) % 4
    return



n = int(input())

arr = [[0] * n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = n * n

snail(0, 0)

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()