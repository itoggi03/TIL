import sys
sys.stdin = open("sample_input_2.txt")

def search(n):
    global cnt, half, root
    if n:
        cnt += 1
        if n == 1:
            root = cnt
            # print(root
        if n == N // 2:
            half = cnt
        search(tree[n][0])

        search(tree[n][1])





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 2 for _ in range(N+1)]

    for i in range(1, N+1):
        if 2*i <= N:
            tree[i][0] = 2 * i
        if 2*i+1 <= N:
            tree[i][1] = 2 * i + 1

    cnt = 0
    root = 0
    half = 0
    # print(tree)

    search(1)

    print('#{} {} {}'.format(tc, root, half))