# JO 1329 별삼각형3
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=608&sca=2020

n = int(input())

if n < 1 or n > 100 or n % 2 == 0:
    print("INPUT ERROR!")
else:
    tmp = 0     # 공백 개수
    star = 1    # 별 개수
    for i in range(n):
        print(' ' * tmp, end='')
        print('*' * star)
        if i < n // 2:
            tmp += 1
            star += 2
        else:
            tmp -= 1
            star -= 2