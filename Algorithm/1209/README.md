# 12/09 JO 1291, 1341, 1303

[toc]

## 1. JO1291 구구단

> 문제 링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=574&sca=20

<br>

### 나의 코드

```python
# 구구단 출력하는 함수
def multi():
    for num in range(1, 10):
        # 처음 입력값 > 끝 입력값
        if s > e:
            for i in range(s, e-1, -1):
                print("{} * {} = {:>2d}".format(i, num, i*num), end="   ")
            if num != 9:
                print()

        # 처음 입력값 < 입력값보다 작을 때
        else:
            for i in range(s, e+1):
                print("{} * {} = {:>2d}".format(i, num, i * num), end="   ")
            if num != 9:
                print()

# 입력
s, e = map(int, input().split())

# s와 e가 2~9 사이의 값이 아니면 에러 문구 출력 후 다시 입력받기 반복
while s > 9 or s < 2 or e > 9 or e < 2:
    print("INPUT ERROR!")
    s, e = map(int, input().split())

# 구구단 함수 호출
multi()
```

<br>

### 입력

```python
2 5
```

<br>

### 출력

```bash
2 * 1 =  2   3 * 1 =  3   4 * 1 =  4   5 * 1 =  5   
2 * 2 =  4   3 * 2 =  6   4 * 2 =  8   5 * 2 = 10   
2 * 3 =  6   3 * 3 =  9   4 * 3 = 12   5 * 3 = 15   
2 * 4 =  8   3 * 4 = 12   4 * 4 = 16   5 * 4 = 20   
2 * 5 = 10   3 * 5 = 15   4 * 5 = 20   5 * 5 = 25   
2 * 6 = 12   3 * 6 = 18   4 * 6 = 24   5 * 6 = 30   
2 * 7 = 14   3 * 7 = 21   4 * 7 = 28   5 * 7 = 35   
2 * 8 = 16   3 * 8 = 24   4 * 8 = 32   5 * 8 = 40   
2 * 9 = 18   3 * 9 = 27   4 * 9 = 36   5 * 9 = 45   
```

<br>

### 회고

- 처음에 계속 80점만 맞게 나왔다. 틀린게 없는데 왜그러나 진짜 이것저것 다 바꿔봤는데도 안되서 포기할때쯤...

  정올은 제출하면 테스트케이스를 100줄까지 공개한다. 그걸 자세히 봤더니 내 코드는 10일 때 구구단이 출력되는 것이다!! 그래서 설마... 하고 봤더니 범위체크를 잘못 해준 탓이었다😪

  **앞으로는 테스트케이스 결과를 자세히 봐보자!!! 범위체크도 꼼꼼이!!**

- format으로 자리수 정해서 출력하는 방법

  ```python
  print("{} * {} = {:>2d}".format(i, num, i*num), end=" ")
  ```

  - {:<2d} : 두자리로 출력. 빈자리를 공백으로 채움. 왼쪽 정렬
  - {:>2d} : 두자리로 출력. 빈자리를 공백으로 채움. 오른쪽 정렬

<br>

<br>

<br>

## 2. JO1341 구구단2

> 문제 링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=574&sca=20

<br>

### 나의 코드

```python
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
```

<br>

### 입력

```bash
2 5
```

<br>

### 출력

```bash
2 * 1 =  2   2 * 2 =  4   2 * 3 =  6   
2 * 4 =  8   2 * 5 = 10   2 * 6 = 12   
2 * 7 = 14   2 * 8 = 16   2 * 9 = 18   

3 * 1 =  3   3 * 2 =  6   3 * 3 =  9   
3 * 4 = 12   3 * 5 = 15   3 * 6 = 18   
3 * 7 = 21   3 * 8 = 24   3 * 9 = 27   

4 * 1 =  4   4 * 2 =  8   4 * 3 = 12   
4 * 4 = 16   4 * 5 = 20   4 * 6 = 24   
4 * 7 = 28   4 * 8 = 32   4 * 9 = 36   

5 * 1 =  5   5 * 2 = 10   5 * 3 = 15   
5 * 4 = 20   5 * 5 = 25   5 * 6 = 30   
5 * 7 = 35   5 * 8 = 40   5 * 9 = 45   
```

<br>

### 회고

- JO1291 구구단1과 크게 다를게 없는 문제였다.
- 출력 형식만 바꿔주면 되는 문제여서 for문의 순서만 바꿔서 풀었다.

<br>

<br>

<br>

## 3. JO303 숫자사각형1

> 문제 링크: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2069&sca=20

<br>

### 나의 코드

```python
n, m = map(int, input().split())

num = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        print(num, end=" ")
        num += 1
    print()
```

<br>

### 입력

```bash
4 5
```

<br>

### 출력

```bash
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20
```

<br>

### 회고

- 출력할 숫자를 따로 선언해서 1씩 증가시켜주는 방법을 사용하면 간단하게 풀 수 있다.
- i와 j로 어떻게 해볼 생각은 하지 말자!