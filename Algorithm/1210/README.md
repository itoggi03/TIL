# 12/10 JO 1856, 1304, 2046

[toc]

# JO1856 숫자사각형2

> 문제링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1129&sca=20

### 나의 코드

```bash
# 높이 n, 너비 m
n, m = map(int, input().split())

nums = [[0] * m for _ in range(n)]

# 미리 배열에 숫자들을 지그재그로 넣어놓음
num = 1
for i in range(n):
    # 짝수 행일 때는 순방향으로 숫자 집어넣기
    if i % 2 == 0:
        for j in range(m):
            nums[i][j] = num
            num += 1
    # 홀수 행일 때는 역방향으로 숫자 집어넣기
    else:
        for j in range(m-1, -1, -1):
            nums[i][j] = num
            num += 1

# 출력
for i in range(n):
    for j in range(m):
        print(nums[i][j], end=" ")
    print()
```

### 입력

```bash
4 5
```

### 출력

```bash
1 2 3 4 5 
10 9 8 7 6 
11 12 13 14 15 
20 19 18 17 16
```

### 회고

- 바로 출력을 하려면 복잡하다. 미리 배열에 숫자들을 지그재그로 집어넣고 그것을 순서대로 출력하는 방법이 훨씬 간단하다.

<br>

<br>

# JO1304 숫자사각형3

> 문제링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2070&sca=2010

### 나의 코드

```python
n = int(input())

nums = [[0] * n for _ in range(n)]
num = 1

# 배열에 미리 숫자들을 넣기
# 열방향 우선
for i in range(n):
    for j in range(n):
        nums[j][i] = num
        num += 1

# 출력
for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
```

### 입력

```bash
4
```

### 출력

```bash
1 5 9 13 
2 6 10 14 
3 7 11 15 
4 8 12 16
```

### 회고

- 숫자사각형2랑 비슷하다. 열방향인것만 다르게 처리 해주면 되는 문제였다.

<br>

<br>

# JO2046 숫자사각형4

> 문제링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1316&sca=20

### 나의 코드

```python
# n: 한 변의 길이 / m: 종류
n, m = map(int, input().split())

num = 1
nums = [[0] * n for _ in range(n)]

# 종류 1일 경우
if m == 1:
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
        print()
        num += 1

# 종류 2일 경우
elif m == 2:
    # 숫자 미리 넣어놓고
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                nums[i][j] = num
                num += 1
        else:
            for j in range(n):
                num -= 1
                nums[i][j] = num
    # 출력
    for i in range(n):
        for j in range(n):
            print(nums[i][j], end=" ")
        print()

# 종류 3일 경우
elif m == 3:
    a = 1 # 행 별 더해지는 수
    # 숫자 미리 넣어놓고,
    for i in range(n):
        for j in range(n):
            nums[i][j] = num
            num += a
        a += 1
        num = a

    # 출력
    for i in range(n):
        for j in range(n):
            print(nums[i][j], end=" ")
        print()
```

### 입력

```python
4 3
```

### 출력

```python
1 2 3 4 
2 4 6 8 
3 6 9 12 
4 8 12 16
```

### 회고

- 숫자사각형 1~3을 풀었다면 무난히 풀 수 있는 문제였다.