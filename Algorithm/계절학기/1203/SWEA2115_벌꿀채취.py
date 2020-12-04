import sys
sys.stdin = open("sample_input2.txt", "r")

def choose(total, r, c):
    global first, second

    # r행의 c~c+M열의 부분집합을 구하여 꿀의 양이 C 이하이면서 수익이 최대인 지점을 찾음
    for i in range(1<<M):
        sum_profit = 0
        sum_honey = 0
        for j in range(M):
            if i & (1<<j):
                sum_profit += honey[r][j+c] ** 2
                sum_honey += honey[r][j+c]

        # first보다 수익이 클 때
        if sum_honey <= C and sum_profit > first[0]:
            # first랑 겹치면 기존 first 버리고 현재 정보 저장
            if r == first[1] and first[2] <= c < first[2]+M:
                first = [sum_profit, r, c]

            # first랑 겹치지 않으면 기존 first는 second로, first에 현재 정보 저장
            else:
                second = first[:]
                first = [sum_profit, r, c]

        # first보다 수익이 작을 때
        elif sum_honey <= C:
            # second보다 크고, first랑 겹치지 않으면 second에 현재 정보 저장
            if sum_profit > second[0] and (r != first[1] or c >= first[2]+M or c < first[2]):
                second = [sum_profit, r, c]





for tc in range(1, int(input())+1):
    # 벌통의 크기(N), 벌통의 개수(M), 꿀을 채취할 수 있는 최대 양(C)
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 수익, 행, 열
    first = [0, 0, 0]
    second = [0, 0, 0]

    for i in range(N):
        for j in range(N-M+1):
            choose(0, i, j)

    print('#{} {}'.format(tc, first[0] + second[0]))