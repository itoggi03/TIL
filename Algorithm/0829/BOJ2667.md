# 0829 BOJ2667: 단지번호 붙이기



## 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![image-20200830011208777](BOJ2667.assets/image-20200830011208777.png)

##### 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.



##### 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.





## 나의 코드

```python
# BOJ2667: 단지번호 붙이기
# https://www.acmicpc.net/problem/2667

import sys
sys.stdin = open("input.txt", "r")

# 인덱스가 보드의 범위를 넘어가는지 확인해주는 함수
def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

# 단지별로 같은 숫자로 바꿔주는 함수
# 해당 좌표의 상하좌우 방향을 보고 주변에 1인 곳이 있으면 그곳을 num으로 바꿔준 후 그 좌표에서 다시 complex 함수 호출
def complex(x, y):
    global num, cnt
    BRD[x][y] = num     # 해당 좌표의 값을 num으로 바꿈
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if check(newX, newY) and BRD[newX][newY] == 1:
            BRD[newX][newY] = num
            cnt += 1        # 바꾼 횟수 카운트(== 단지 내 집의 수)
            complex(newX, newY)

# 입력
N = int(input())
BRD = [list(map(int, input())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 2     # 단지 숫자를 2부터 시작(1부터 하면 체크하는데 헷갈리므로)
cnt = 0
hnum = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 1:
            complex(i, j)
            hnum.append(cnt)
            num += 1    # 단지 수 카운트
            cnt = 0

# 결과 출력
print(num - 2)      # num을 2부터 시작했으므로 단지 수는 num-2
hnum.sort()         # 단지 내 집 숫자 오름차순 정렬
for i in hnum:      # 한줄 씩 단지 별 집 숫자 출력
    print(i + 1)    # complex 함수에서 처음 시작 좌표를 바꿔준 것을 체크 안했으므로 +1 해서 출력
```

1. 보드의 (0,0)부터 탐색하며 1을 찾는다. 1을 찾았을 경우, 그 좌표의 상하좌우를 보며 1일 경우 단지 번호로 바꿔주는 complex 함수를 호출
2. complex 함수: 해당 좌표의 상하좌우에 1이 있을 경우 그 부분을 단지 번호로 바꿔주고, 그 좌표로 또 complex 함수를 호출 -> 각 집의 이웃을 모두 찾을 수 있음
3. check 함수: 인덱스가 보드 범위를 넘어가지 않는지 체크하는 함수



## 틀린 코드

```python
# https://www.acmicpc.net/problem/2667
# BOJ2667: 단지번호 붙이기
import sys
sys.stdin = open("input.txt", "r")

def check(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

def complex(x, y):
    global num
    cnt = 1
    home_num = 0
    BRD[x][y] = num
    while cnt != 0:
        cnt = 0
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if check(newX, newY) and BRD[newX][newY] == 1:
                BRD[newX][newY] = num
                next_d = d
                cnt += 1
                home_num += 1
        if cnt == 0:
            num += 1
            return home_num
        x += dx[next_d]
        y += dy[next_d]

N = int(input())
BRD = [list(map(int, input())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 2
home = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 1:
            home.append(complex(i, j))

print(num - 2)
home.sort()
for i in home:
    print(i + 1)
```

- 틀린 이유: complex 함수에서 해당 좌표의 상하좌우를 체크하면서 1인 부분이 있으면 그 부분의 좌표를 단지 번호로 바꾸고 그 좌표로 가서 다시 상하좌우를 체크하는 방식으로 코드를 짬 => 단지의 모양에 따라 이웃임에도 불구하고 체킹이 안되는 집이 생김

- 따라서 모든 이웃을 체크할 수 있도록 이웃인게 확인되면 그 이웃의 상하좌우를 또 확인하는 방식으로 코드를 수정하였다.