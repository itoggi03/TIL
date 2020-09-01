# SWEA 토너먼트 카드게임

import sys
sys.stdin = open("sample_input3.txt", "r")

# 가위바위보 승자의 인덱스를 반환하는 함수
def win(a, b):
    if (num[a-1]-num[b-1] == 1) or (num[a-1]-num[b-1] == -2):
        return a
    elif num[a-1] == num[b-1]:
        return min(a, b)
    else:
        return b

# 계속 두 그룹으로 나누어 승자를 구하는 함수
def matching(i, j):
    if i == j:
        return i
    i_w = matching(i, (i+j)//2)
    j_w = matching((i+j)//2+1, j)
    return win(i_w, j_w)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    i = 1   # 시작 번호
    j = N   # 끝 번호

    result = matching(i, j)

    print('#{} {}'.format(test_case, result))
