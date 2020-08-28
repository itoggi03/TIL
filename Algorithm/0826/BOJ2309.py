# https://www.acmicpc.net/problem/2309
import random

# 입력 받아서 num_list에 저장
num_list = []
for i in range(9):
    num_list.append(int(input()))

# num_list에서 7개의 숫자를 랜덤으로 뽑아(sample함수 이용) 그 합이 100이 될 경우를 판별
# 합이 100이 될 경우 result에 해당 숫자 리스트 넣고 while문 종료
flag = False
while not flag:
    tmp = random.sample(num_list, k=7)
    if sum(tmp) == 100:
        flag = True
        result = tmp

# 결과값 정렬
dwarfs = sorted(result)

# 결과값 출력
print('\n'.join(map(str, dwarfs)))
