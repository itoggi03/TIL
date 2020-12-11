# JO 1307 문자사각형1
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2071&sca=2010

n = int(input())

s = 65  # 'A'의 아스키코드
arr = [[0] * n for _ in range(n)]

# 미리 배열에 규칙에 맞게 알파벳 넣어놓음
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = chr(s)
        if s == 90: # 'Z'일 경우 다음 알파벳은 'A'
            s = 65
        else:
            s+= 1

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()