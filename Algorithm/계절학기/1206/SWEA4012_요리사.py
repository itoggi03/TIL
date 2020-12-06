# SWEA_4012 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE

import sys
sys.stdin = open("sample_input.txt", "r")


# 각각의 경우 맛의 점수 차를 계산하는 함수
def best(arr1, arr2):
    score1 = 0
    score2 = 0
    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                score1 += S[arr1[i]-1][arr1[j]-1]
                score2 += S[arr2[i]-1][arr2[j]-1]
    return abs(score1-score2)


# n개의 배열 중 r개를 순서 상관없이 뽑아내는 함수(조합)
def comb(n, r):
    global result, min_result
    if r == 0:
        tmp2 = []
        # 뽑아낸 배열과 겹치지 않는 배열 만들기
        for i in range(1, N+1):
            if i not in tmp1:
                tmp2.append(i)

        # N//2개씩 나눠서 각각에 대한 맛의 점수를 계산하는 함수 호출
        result = best(tmp1, tmp2)

        # 현재 가지고 있는 최소값보다 작으면 값 업데이트
        if min_result > result:
            min_result = result
    elif n < r:
        return
    else:
        tmp1[r - 1] = a[n - 1]
        comb(n-1, r-1)
        comb(n-1, r)


for tc in range(1, int(input())+1):
    N = int(input())    # 재료의 수
    S = [list(map(int, input().split())) for _ in range(N)]     # N*N개의 시너지 값들

    a = []
    tmp1 = [0] * (N // 2)
    for i in range(N):
        a.append(i + 1)

    result = 0
    min_result = 10000000
    comb(N, N//2)

    print('#{} {}'.format(tc, min_result))


