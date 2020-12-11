# JO 1314 문자사각형2
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2072&sca=20

n = int(input())

s = 65
arr = [[0] * n for _ in range(n)]

# 미리 배열에 값 넣어놓기
for i in range(n):
    # 짝수행은 열방향 순방향
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = chr(s)
            # Z 다음 A
            if s == 90:
                s = 65
            else:
                s += 1

    # 홀수행은 열방향 역방향
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = chr(s)
           # Z 다음 A
           if s == 90:
                s = 65
            else:
                s += 1

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()