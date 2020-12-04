# SWEA_5658 [모의 SW 역량테스트] 보물상자 비밀번호
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE
import sys
sys.stdin = open("sample_input.txt", "r")


# 시계방향으로 한칸씩 회전시켜주는 함수
def rotation():
    global nums
    tmp = [0] * N
    tmp[0] = nums[-1]
    tmp[1:] = nums[:-1]
    nums = tmp[:]


for tc in range(1, int(input())+1):
    # N: 숫자 개수, K: K번째로 큰 수를 출력
    N, K = map(int, input().split())
    nums = list(input())    # N개의 숫자들
    M = N // 4   # 회전 횟수

    # 회전 횟수만큼 rotation 함수를 호출하고, 호출할 때마다 각각의 수를 set에 집어넣어서 중복을 제거하여 저장
    num_list = set()
    for i in range(M):
        rotation()
        for j in range(0, N-M+1, M):
            # 16진수를 10진수로 변환하여 저장
            num_list.add(int(''.join(nums[j:j+M]), 16))

    # set을 list로 바꿔주고, 내림차순 정렬
    result = list(num_list)
    result.sort(reverse=True)

    # 출력
    print('#{} {}'.format(tc, result[K-1]))