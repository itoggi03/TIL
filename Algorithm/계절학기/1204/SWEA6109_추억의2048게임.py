# SWEA_6109 추억의 2048게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ
from collections import deque
import sys
sys.stdin = open("s_input.txt", "r")


# 시계 방향으로 90도 회전시켜주는 함수
def rotation(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp


# 위쪽으로 미는 함수
def push(arr):
    q = deque()

    # 배열의 열방향, 역방향으로 값을 순회하면서 deque에 넣어주기
    for i in range(N):
        idx = 0
        for j in range(N):
            if arr[j][i] != 0:
                q.append(arr[j][i])
                arr[j][i] = 0

        # q에 값이 있을 동안 두개씩 꺼내서 같으면 합쳐서 배열에 넣어주고, 다르면 앞에 값 하나만 배열에 넣어줌
        while q:
            if len(q) > 1:
                a, b = q.popleft(), q.popleft()
                if a == b:
                    arr[idx][i] = a + b
                    idx += 1
                else:
                    arr[idx][i] = a
                    q.appendleft(b)
                    idx += 1
            # q에 값이 한 개일 경우 꺼내서 배열에 넣어줌
            else:
                arr[idx][i] = q.popleft()
    return arr


for tc in range(1, int(input())+1):
    # 격자판 크기 N, 문자열 S(up, down, left, right)
    N, S = input().split()
    N = int(N)
    num_arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    # 위로 밀 때
    if S == 'up':
        result = push(num_arr)
    # 왼쪽으로 밀 때: 한 번 회전 후 push, 그리고 다시 세 번 회전
    elif S == 'left':
        result = rotation(num_arr)
        result = push(result)
        result = rotation(result)
        result = rotation(result)
        result = rotation(result)
    # 아래쪽으로 밀 때: 두 번 회전 후 push, 그리고 다시 두 번 회전
    elif S == 'down':
        result = rotation(num_arr)
        result = rotation(result)
        result = push(result)
        result = rotation(result)
        result = rotation(result)
    # 오른쪽으로 밀 때: 세 번 회전 후 push, 그리고 다시 한 번 회전
    elif S == 'right':
        result = rotation(num_arr)
        result = rotation(result)
        result = rotation(result)
        result = push(result)
        result = rotation(result)

    # 출력
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(result[i][j], end = ' ')
        print()