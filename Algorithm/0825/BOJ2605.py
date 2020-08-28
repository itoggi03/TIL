# https://www.acmicpc.net/problem/2605

# 학생 수 N명 입력 받기
N = int(input())
# 주어진 학생들이 뽑은 번호 list로 입력받기
# 인덱스가 헷갈리지 않도록 맨 앞에 0을 주고 1번째부터 입력 받음
num = [0] + list(map(int, input().split()))

result = [0]

# 학생들의 최종 순서: 원래 자신의 순서에서 뽑은 숫자만큼 앞으로 가는 것이기 때문에 (원래 순서 - 뽑은 숫자)번째 자리에 들어가게 된다.
for i in range(1, N+1):
    result.insert(i-num[i], i)

print(' '.join(map(str, result[1:])))