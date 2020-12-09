# JO 1291 구구단
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=574&sca=20

# 구구단 출력하는 함수
def multi():
    # 처음 입력값 > 끝 입력값
    if s > e:
        for i in range(s, e-1, -1):
            for num in range(1, 10):
                print('{} * {} = {:>2d}'.format(i, num, i*num), end="   ")
                if num == 3 or num == 6:
                    print()
            print()
            print()

    # 처음 입력값 < 입력값보다 작을 때
    else:
        for i in range(s, e+1):
            for num in range(1, 10):
                print('{} * {} = {:>2d}'.format(i, num, i*num), end="   ")
                if num == 3 or num == 6:
                    print()
            print()
            print()


# 입력
s, e = map(int, input().split())

# s와 e가 2~9 사이의 값이 아니면 에러 문구 출력 후 다시 입력받기 반복
while s > 9 or s < 2 or e > 9 or e < 2:
    print("INPUT ERROR!")
    s, e = map(int, input().split())

# 구구단 함수 호출
multi()
