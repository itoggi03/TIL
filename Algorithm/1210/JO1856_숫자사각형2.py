# JO1856 숫자사각형2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1129&sca=20


# 높이 n, 너비 m
n, m = map(int, input().split())

nums = [[0] * m for _ in range(n)]

# 미리 배열에 숫자들을 지그재그로 넣어놓음
num = 1
for i in range(n):
    # 짝수 행일 때는 순방향으로 숫자 집어넣기
    if i % 2 == 0:
        for j in range(m):
            nums[i][j] = num
            num += 1
    # 홀수 행일 때는 역방향으로 숫자 집어넣기
    else:
        for j in range(m-1, -1, -1):
            nums[i][j] = num
            num += 1

# 출력
for i in range(n):
    for j in range(m):
        print(nums[i][j], end=" ")
    print()
