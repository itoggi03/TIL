import sys
sys.stdin = open("sample_input.txt", "r")


# 모든 부분집합을 만들어서 제한 칼로리 내에서 최대 점수를 출력하는 함수
def solution():
    tmp = 0

    for i in range(1<<N):
        tmp_s = 0
        tmp_k = 0
        for j in range(N):
            if i & (1<<j):
                tmp_s += score[j][0]
                tmp_k += score[j][1]
        if tmp_k <= L:
            if tmp <= tmp_s:
                tmp = tmp_s
    return tmp


T = int(input())

for tc in range(1, T+1):
    # N: 재료 개수, L: 최대 칼로리
    N, L = map(int, input().split())

    score = []
    for i in range(N):
        T, K = map(int, input().split())
        score.append([T, K])

    print('#{} {}'.format(tc, solution()))