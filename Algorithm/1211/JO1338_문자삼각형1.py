# JO 1338 문자삼각형1
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2074&sca=20

N = int(input())

arr = [[0] * N for _ in range(N)]

s = 65  # 'A'의 번호
t = -1
# 배열에 조건 맞춰 숫자 넣기
for i in range(N-1, -1, -1):
    for j in range(N-1, t, -1):
        arr[N-j+t][j] = chr(s)
        if s == 90:
            s = 65
        else:
            s += 1
    t += 1

# 출력
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            print(" ", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()