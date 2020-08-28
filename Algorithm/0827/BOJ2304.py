# https://www.acmicpc.net/problem/2304

# 입력 받아오기
N = int(input())
LH = sorted([list(map(int, input().split())) for _ in range(N)])

# 오른쪽 끝의 인덱스를 end에 받아옴
end = LH[-1][0]

# 높이만 리스트에 받아오기
height = [0] * (LH[-1][0]+1)
for i in range(N):
    height[LH[i][0]] = LH[i][1]

# 높이가 젤 높은 곳의 인덱스를 받아옴
max_idx = height.index(max(height))

# 왼쪽
tmp = 0
total = 0
for i in range(max_idx+1):
    if height[i] > tmp:
        tmp = height[i]
    total += tmp

# 오른쪽
tmp = 0
for j in range(end, max_idx, -1):
    if height[j] > tmp:
        tmp = height[j]
    total += tmp

print(total)
