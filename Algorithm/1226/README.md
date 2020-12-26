# 12/26 JO 1337 달팽이 삼각형

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=609&sca=2020

<br>

### 나의 코드

```jsx
# 배열 인덱스 넘었는지 확인해주는 함수
def check(x, y):
    if x < N and x >= 0 and y < N and y >= 0:
        return True
    else:
        return False

# 달팽이 모양으로 숫자 채워주는 함수
def snail(x, y):
    num = 0
    d = 0
    arr[x][y] = num
    num += 1
    visited[x][y] = 1
    chk = 1

    # 숫자 채워진 개수(chk)가 채워져야할 수의 개수(cnt)랑 같아질 때까지 반복
    while chk < cnt:
        newX = x + dr[d]
        newY = y + dc[d]
        # 배열 인덱스를 넘어가지 않고, 방문하지 않았던 곳이라면 숫자 채워넣기
        if check(newX, newY) and not visited[newX][newY]:
            arr[newX][newY] = num
            visited[newX][newY] = 1
            chk += 1
            num = (num+1) % 10  # 0 ~ 9 반복
            x, y = newX, newY

        # 이미 채워진 곳을 만났거나 인덱스를 넘어갈 경우 방향 바꾸기
        else:
            # 0, 1, 2 반복
            d = (d+1) % 3
    return

N = int(input())

arr = [[''] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 오른쪽 아래/왼쪽/위쪽
dr = [1, 0, -1]
dc = [1, -1, 0]

# 숫자 개수 계산: N + (N-1) + (N-2) + ... + 1
cnt = 0
for i in range(1, N+1):
    cnt += i

snail(0, 0)

# 출력
for i in range(N):
    for j in range(N):
        if arr[i][j] != '':
            print(arr[i][j], end=" ")
    print()
```

<br>

### 입력

```jsx
6
```

<br>

### 출력

```jsx
0 
4 1 
3 5 2 
2 0 6 3 
1 9 8 7 4 
0 9 8 7 6 5
```

<br>

### 회고

- 오른쪽 아래, 왼쪽, 위쪽을 반복하며 숫자를 채워나가는 방법으로 풀었다.
- 방향을 바꿀 경우는 인덱스가 넘어갈 경우 혹은 이미 채워진 곳을 만났거나이다.