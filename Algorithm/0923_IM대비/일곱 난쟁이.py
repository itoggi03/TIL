# BOJ2309 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

# 입력
height = []
for i in range(9):
    height.append(int(input()))

n = len(height)    

# 부분집합의 길이가 7이고 합이 100일 떄 for문 탈출
tmp = []
for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            tmp.append(height[j])
    if len(tmp) == 7 and sum(tmp) == 100:
        break
    tmp = []

# 정렬 후 출력
tmp.sort()
for i in tmp:
    print(i)