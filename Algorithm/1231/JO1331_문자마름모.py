# JO1331 문자마름모
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2073&sca=2020

# A~Z : 65~90

# 인덱스 넘어갔는지 확인해주는 함수
def check(x, y):
    if x < N and x >= 0 and y < N and y >= 0:
        return True
    else:
        return False


# 채워야할 곳이 아닌 곳을 가리키는지 확인해주는 함수
def check2(x, y, d):
    if d == 0:
        if arr[x-1][y] != ' ' and arr[x][y+1] != ' ':
            return False
    if d == 1:
        if arr[x-1][y] != ' ' and arr[x][y-1] != ' ':
            return False
    if d == 2:
        if arr[x][y-1] != ' ' and arr[x+1][y] != ' ':
            return False
    return True


def rhombus(x, y):
    num = 65
    d = 0
    arr[x][y] = chr(num)
    num += 1
    chk = 1

    while chk < cnt:
        newX = x + dr[d]
        newY = y + dc[d]
        if check(newX, newY) and arr[newX][newY] == ' ' and check2(newX, newY, d):
            arr[newX][newY] = chr(num)

            # Z -> A
            if num == 90:
                num = 65
            else:
                num += 1
            x, y = newX, newY
            chk += 1
        else:
            d = (d+1) % 5


n = int(input())    # 마름모 한 변의 길이
N = (2 * n) - 1     # 배열 크기

dr = [1, 1, -1, -1, 0]
dc = [-1, 1, 1, -1, -1]

arr = [[' '] * N for _ in range(N)]
cnt = ((N * N) // 2) + 1    # 채워야하는 문자 개수

rhombus(0, N // 2)

# 출력
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()