# JO 1303 숫자사각형1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2069&sca=20

n, m = map(int, input().split())

num = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        print(num, end=" ")
        num += 1
    print()


