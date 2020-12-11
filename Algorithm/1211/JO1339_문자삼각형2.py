# JO 1339 문자삼각형2
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2075&sca=20

N = int(input())
s = 65
c = N // 2

# 범위를 벗어나는 입력일 경우 에러 문구 출력
if N % 2 == 0 or N < 1 or N > 100:
    print("INPUT ERROR")
else:
    arr = [[0] * N for _ in range(N)]

    # 행의 시작점: 열번호, 행의 끝점: N-1-열번호
    for j in range(N // 2, -1, -1):
        for i in range(c, N-1-c+1):
            arr[i][j] = chr(s)
            if s == 90:
                s = 65
            else:
                s += 1
        c -= 1

    # 출력
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                print(" ", end=" ")
            else:
                print(arr[i][j], end=" ")
        print()