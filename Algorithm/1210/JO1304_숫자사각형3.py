# JO 1304 숫자사각형3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2070&sca=2010

n = int(input())

nums = [[0] * n for _ in range(n)]
num = 1

# 배열에 미리 숫자들을 넣기
# 열방향 우선
for i in range(n):
    for j in range(n):
        nums[j][i] = num
        num += 1

# 출력
for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()

