# 12/31 JO1331 문자마름모

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2073&sca=2020

<br>

### 나의 코드

```python
# 인덱스 넘어갔는지 확인해주는 함수
def check(x, y):
    if x < N and x >= 0 and y < N and y >= 0:
        return True
    else:
        return False

# 채워야할 곳이 아닌 곳을 가리키는지 확인해주는 함수
def check2(x, y, d):
    if d == 0:
        if arr[x-1][y] != ' ' and arr[x][y+1] != ' ':
            return False
    if d == 1:
        if arr[x-1][y] != ' ' and arr[x][y-1] != ' ':
            return False
    if d == 2:
        if arr[x][y-1] != ' ' and arr[x+1][y] != ' ':
            return False
    return True

def rhombus(x, y):
    num = 65
    d = 0
    arr[x][y] = chr(num)
    num += 1
    chk = 1

    while chk < cnt:
        newX = x + dr[d]
        newY = y + dc[d]
        if check(newX, newY) and arr[newX][newY] == ' ' and check2(newX, newY, d):
            arr[newX][newY] = chr(num)
            
            # Z -> A
            if num == 90:
                num = 65
            else:
                num += 1
            x, y = newX, newY
            chk += 1
        else:
            d = (d+1) % 5

n = int(input())    # 마름모 한 변의 길이
N = (2 * n) - 1     # 배열 크기

dr = [1, 1, -1, -1, 0]
dc = [-1, 1, 1, -1, -1]

arr = [[' '] * N for _ in range(N)]
cnt = ((N * N) // 2) + 1    # 채워야하는 문자 개수

rhombus(0, N // 2)

# 출력
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
```

<br>

### 입력

```bash
4
```

<br>

### 출력

```bash
			A       
    B M L     
  C N U T K   
D O V Y X S J 
  E P W R I   
    F Q H     
      G
```

<br>

### 회고

- 달팽이 사각형과 비슷하게 푼다. 하지만 다음 위치가 인덱스를 넘지 않고, 비어있다면 채우는 방식으로는 풀리지 않는다. 대각선으로 움직이기 때문에 위의 예시 같은 경우 O 다음에 D 아래쪽으로 가게 되는 현상이 발생한다. 따라서 check2라는 함수를 하나 더 만들어주어 예외처리를 해주었다.
  - 왼쪽 아래 대각선 방향으로 움직일 경우 위, 오른쪽이 문자로 채워져 있으면 False 반환
  - 오른쪽 아래 대각선 방향으로 움직일 경우 위, 왼쪽이 문자로 채워져 있으면 False 반환
  - 오른쪽 위 대각선 방향으로 움직일 경우 왼쪽, 아래가 문자로 채워져 있으면 False 반환