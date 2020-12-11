# 12/11 JO 1307 / 1314 / 1338 / 1339

[toc]

# 1. JO1307 문자 사각형1

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2071&sca=2010

<br>

### 나의 코드

```python
n = int(input())

s = 65  # 'A'의 아스키코드
arr = [[0] * n for _ in range(n)]

# 미리 배열에 규칙에 맞게 알파벳 넣어놓음
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = chr(s)
        if s == 90: # 'Z'일 경우 다음 알파벳은 'A'
            s = 65
        else:
            s+= 1

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
```

<br>

### 입력

```python
5
```

<br>

### 출력

```python
Y T O J E 
X S N I D 
W R M H C 
V Q L G B 
U P K F A
```

<br>

### 회고

- python의 `ord`와 `chr`만 알면 쉽게 풀 수 있는 문제였다.

<br>

<br>

# 2. JO1314 문자 사각형2

>문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2072&sca=20

<br>

### 나의 코드

```python
n = int(input())

s = 65
arr = [[0] * n for _ in range(n)]

# 미리 배열에 값 넣어놓기
for i in range(n):
    # 짝수행은 열방향 순방향
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = chr(s)
            # Z 다음 A
            if s == 90:
                s = 65
            else:
                s += 1

    # 홀수행은 열방향 역방향
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = chr(s)
           # Z 다음 A
           if s == 90:
                s = 65
            else:
                s += 1

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
```

<br>

### 입력

```python
4
```

<br>

### 출력

```python
A H I P 
B G J O 
C F K N 
D E L M
```

<br>

### 회고

- 열 별로 순방향 역방향 다르게 해서 미리 배열에 넣어준 뒤 출력하면 되는 문제이다.

<br>

<br>

# 3. JO 1338 문자 삼각형1

>문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2074&sca=20

<br>

### 나의 코드

```python
N = int(input())

arr = [[0] * N for _ in range(N)]

s = 65  # 'A'의 번호
t = -1
# 배열에 조건 맞춰 숫자 넣기
for i in range(N-1, -1, -1):
    for j in range(N-1, t, -1):
        arr[N-j+t][j] = chr(s)
        if s == 90:
            s = 65
        else:
            s += 1
    t += 1

# 출력
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            print(" ", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
```

<br>

### 입력

```python
5
```

<br>

### 출력

```python
				A 
      B F 
    C G J 
  D H K M 
E I L N O
```

<br>

### 회고

- 인덱스를 맞춰서 대각선 왼쪽 아래 방향으로 알파벳을 하나씩 늘려가면서 저장하는게 어려웠다.

- t를 선언해서 이용했던 것이 도움이 되었다.

- 알파벳이 채워지는 순서대로 인덱스를 표기해보면 다음과 같다.

  (0, 3) (1, 2) (2, 1) (3, 0) | (1, 3) (2, 2) (3, 1) | (2, 3) (3, 2) | (3, 3)

  이 순서대로 인덱스를 맞추도록 두개의 for문을 이용해서 코드를 짰다.

- 아직도 헷갈린다😂

<br>

<br>

# 4. JO 1339 문자 삼각형2

>문제 링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2075&sca=20

<br>

### 나의 코드

```python
N = int(input())
s = 65
c = N // 2

# 범위를 벗어나는 입력일 경우 에러 문구 출력
if N % 2 == 0 or N < 1 or N > 100:
    print("INPUT ERROR")
else:
    arr = [[0] * N for _ in range(N)]

    # 행의 시작점: 열번호, 행의 끝점: N-1-열번호
    for j in range(N // 2, -1, -1):
        for i in range(c, N-1-c+1):
            arr[i][j] = chr(s)
            if s == 90:
                s = 65
            else:
                s += 1
        c -= 1

    # 출력
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                print(" ", end=" ")
            else:
                print(arr[i][j], end=" ")
        print()
```

<br>

### 입력

```python
5
```

<br>

### 출력

```python
E         
F B       
G C A     
H D       
I
```

<br>

### 회고

- 인덱스 맞추면서 코드를 짜는 것에 아직 익숙한 정도는 아닌 것 같다.
- 열별로 행의 시작 인덱스와 끝 인덱스를 열 인덱스와의 관계식으로 만들어본다.
- 열우선으로 행을 하나씩 증가시키며 값을 채워넣는다.