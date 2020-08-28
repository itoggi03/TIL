# https://www.acmicpc.net/problem/2491
N = int(input())
numbers = list(map(int, input().split()))
tmp = numbers[0]
cnt= 0
result = []

for i in numbers:
    if i >= tmp:
        cnt += 1
        tmp = i
    else:
        tmp = i
        result.append(cnt)
        cnt = 1
result.append(cnt)
cnt = 0

for i in numbers:
    if i <= tmp:
        cnt += 1
        tmp = i
    else:
        tmp = i
        result.append(cnt)
        cnt = 1
result.append(cnt)

print(max(result))
