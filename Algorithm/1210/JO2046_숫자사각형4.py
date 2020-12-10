# JO 2046 숫자사각형4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1316&sca=20

# n: 한 변의 길이 / m: 종류
n, m = map(int, input().split())

num = 1
nums = [[0] * n for _ in range(n)]

# 종류 1일 경우
if m == 1:
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
        print()
        num += 1

# 종류 2일 경우
elif m == 2:
    # 숫자 미리 넣어놓고
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                nums[i][j] = num
                num += 1
        else:
            for j in range(n):
                num -= 1
                nums[i][j] = num
    # 출력
    for i in range(n):
        for j in range(n):
            print(nums[i][j], end=" ")
        print()

# 종류 3일 경우
elif m == 3:
    a = 1 # 행 별 더해지는 수
    # 숫자 미리 넣어놓고,
    for i in range(n):
        for j in range(n):
            nums[i][j] = num
            num += a
        a += 1
        num = a

    # 출력
    for i in range(n):
        for j in range(n):
            print(nums[i][j], end=" ")
        print()