# JO 1719 별삼각형2
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=992&sca=2020

n, m = map(int, input().split())

if n < 1 or n > 100 or n % 2 == 0 or m < 1 or m > 4:
    print("INPUT ERROR!")
else:
    if m == 1:
        tmp = 1 # 공백 개수
        for i in range(n):
            print('*' * tmp)
            if i < n // 2:
                tmp += 1
            else:
                tmp -= 1
    elif m == 2:
        tmp = n // 2    # 공백 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * ((n//2+1) - tmp))
            if i < n // 2:
                tmp -= 1
            else:
                tmp += 1
    elif m == 3:
        tmp = 0     # 공백 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * (n - tmp*2))
            if i < n //2:
                tmp += 1
            else:
                tmp -= 1
    elif m == 4:
        tmp = 0     # 공백 개수
        star = n // 2 + 1   # 별 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * star)
            if i < n // 2:
                tmp += 1
                star -= 1
            else:
                star += 1


