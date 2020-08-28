# https://www.acmicpc.net/problem/2635

# 첫번째 숫자를 입력 받음
first_num = int(input())
m_len = 0

# 두번쨰 숫자를 1~(첫번째 숫자)의 범위로 for문 반복
for i in range(1, first_num+1):
    # n1 : 첫번째 숫자
    # n2 : 두번째 숫자
    # n3 : 세번째 숫자

    # n1, n2, n3 초기화
    n1 = first_num
    n2 = i
    n3 = 0
    # 임시리스트 tmp를 n1, n2가 담긴 리스트로 초기화
    tmp = [n1, n2]

    # (n1 - n2)가 음의 정수가 아닐 때까지 while문 반복
    # n3에 (n1 - n2)를 넣고 이걸 tmp(임시 리스트)에 append 해서 리스트를 만들어줌
    while n1-n2 >= 0:
         n3 = n1-n2
         tmp.append(n3)

         # n1, n2 업데이트
         n1 = n2
         n2 = n3

    # while문이 끝난 후 tmp의 길이를 m_len과 비교 -> 최대값 업데이트
    # m_len에 최대 개수 저장, result에 최대 개수의 수들을 저장
    if len(tmp) >= m_len:
        m_len = len(tmp)
        result = tmp

# 결과 출력
print(m_len)
print(' '.join(map(str, result)))