# JO 1523 별삼각형1
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=795&sca=2020

n, m = map(int, input().split())

if n < 1 or n > 100 or m < 1 or m > 3:
    print("INPUT ERROR!")
else:
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n, 0, -1):
            print('*' * i)
    elif m == 3:
        tmp = n - 1 # 출력할 공백의 개수
        for i in range(1, 1+2*(n-1)+1, 2):
            print(' ' * tmp, end='')
            print('*' * i)
            tmp -= 1




