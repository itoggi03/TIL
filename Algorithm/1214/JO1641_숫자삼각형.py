# JO 1641 숫자삼각형
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=914&sca=2020

n, m = map(int, input().split())

if n < 1 or n > 100 or n % 2 == 0 or m < 1 or m > 3:
    print("INPUT ERROR!")
else:
    # 종류 1
    if m == 1:
        num = 1
        arr = [[0] * n for _ in range(n)]
        # 미리 배열에 조건 맞춰 숫자 넣어놓고,
        for i in range(1, n+1):
            if i % 2 == 1:
                for j in range(i):
                    arr[i-1][j] = num
                    num += 1
            else:
                for j in range(i-1, -1, -1):
                    arr[i-1][j] = num
                    num += 1
        # 출력
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 0:
                    print(arr[i][j], end=" ")
            print()
    # 종류 2
    elif m == 2:
        idx = 0
        num = 0
        arr = [[-1] * (2*n-1) for _ in range(2*n-1)]
        # 미리 배열에 조건 맞춰 숫자 넣어놓고,
        for i in range(2*n-1, 0, -2):
            for j in range(i):
                arr[idx][j+idx] = num
            num += 1
            idx += 1

        # 출력
        for i in range(2*n-1):
            for j in range(2*n-1):
                if arr[i][j] != -1:
                    print(arr[i][j], end=" ")
                else:
                    print(' ', end=" ")
            print()
    # 종류 3
    elif m == 3:
        num = 1
        idx = 1
        for i in range(n):
            num = 1
            for j in range(idx):
                print(num, end=" ")
                num += 1
            # 중간 라인을 기준으로 숫자 개수 조절
            if i < n // 2:
                idx += 1
            else:
                idx -= 1
            print()



