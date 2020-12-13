# JO 1523, 1719, 1329

[toc]

## 1. JO1523 별삼각형1

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=795&sca=2020

<br>

### 나의코드

```python
n, m = map(int, input().split())

if n < 1 or n > 100 or m < 1 or m > 3:
    print("INPUT ERROR!")
else:
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n, 0, -1):
            print('*' * i)
    elif m == 3:
        tmp = n - 1 # 출력할 공백의 개수
        for i in range(1, 1+2*(n-1)+1, 2):
            print(' ' * tmp, end='')
            print('*' * i)
            tmp -= 1
```

<br>

### 입력

```python
4 3
```

<br>

### 출력

```python
   *
  ***
 *****
*******
```

<br>

### 회고

- 종류 1, 2는 쉬운 편이고, 종류 3만 약간의 생각이 필요했다.
- 종류 3은 공백의 개수가 하나씩 줄어드는 것을 이용하여 출력할 공백의 개수를 뜻하는 변수를 선언해서 이를 이용했다.

<br>

<br>

## 2. JO1719 별삼각형2

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=992&sca=2020

<br>

### 나의코드

```python
n, m = map(int, input().split())

if n < 1 or n > 100 or n % 2 == 0 or m < 1 or m > 4:
    print("INPUT ERROR!")
else:
    if m == 1:
        tmp = 1 # 공백 개수
        for i in range(n):
            print('*' * tmp)
            if i < n // 2:
                tmp += 1
            else:
                tmp -= 1
    elif m == 2:
        tmp = n // 2    # 공백 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * ((n//2+1) - tmp))
            if i < n // 2:
                tmp -= 1
            else:
                tmp += 1
    elif m == 3:
        tmp = 0     # 공백 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * (n - tmp*2))
            if i < n //2:
                tmp += 1
            else:
                tmp -= 1
    elif m == 4:
        tmp = 0     # 공백 개수
        star = n // 2 + 1   # 별 개수
        for i in range(n):
            print(' ' * tmp, end='')
            print('*' * star)
            if i < n // 2:
                tmp += 1
                star -= 1
            else:
                star += 1
```

<br>

### 입력

```python
5 4
```

<br>

### 출력

```python
***
 **
  *
  **
  ***
```

<br>

### 회고

- 종류별로 각 케이스를 만들어 별을 출력해주었다.
- 종류 4의 경우, 공백의 개수와 별의 개수를 중간 라인을 기준으로 변화시키며 출력해주었다.

<br>

<br>

## 3. JO1329 별삼각형3

> 문제링크: http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=608&sca=2020

<br>

### 나의코드

```python
n = int(input())

if n < 1 or n > 100 or n % 2 == 0:
    print("INPUT ERROR!")
else:
    tmp = 0     # 공백 개수
    star = 1    # 별 개수
    for i in range(n):
        print(' ' * tmp, end='')
        print('*' * star)
        if i < n // 2:
            tmp += 1
            star += 2
        else:
            tmp -= 1
            star -= 2
```

<br>

### 입력

```python
7
```

<br>

### 출력

```python
*
 ***
  *****
   *******
  *****
 ***
*
```

<br>

### 회고

- 중간 줄을 기준으로 별 개수와 공백 개수를 변화시키며 출력해주었다.

