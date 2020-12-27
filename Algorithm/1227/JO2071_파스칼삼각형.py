# JO2071 파스칼 삼각형
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1335&sca=2020

n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

# 처음 숫자 세팅
arr[0][0] = 1

# 바로 위, 왼쪽 위 숫자 더한 값 채워넣기
for i in range(1, n):
    for j in range(n):
        # 왼쪽 인덱스가 0보다 크거나 같을 경우 왼쪽 위, 바로위 숫자 더한 값 넣기
        if j-1 >= 0:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        # 아닐 경우 바로 위 숫자만 넣기
        else:
            arr[i][j] = arr[i-1][j]

# 종류 1
if m == 1:
    # 출력
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()

# 종류 2
elif m == 2:
    t = -1
    for i in range(n-1, -1, -1):
        if i < n-1:
            print(' ' * t, end=" ")
        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()
        t += 1

# 종류 3
else:
    for j in range(n-1, -1, -1):
        for i in range(n-1, -1, -1):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()

