# https://www.acmicpc.net/problem/1904
# 01타일

def fibo(N):
    a = 1
    b = 0
    for i in range(1, N+1):
        temp = a % 15746
        a = (a + b) % 15746
        b = temp
    return a

N = int(input())

print(fibo(N))