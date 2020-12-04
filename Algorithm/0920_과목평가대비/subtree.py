import sys
sys.stdin = open("sample_input_3.txt")

def subtree(n):
    global cnt
    if n:
        cnt += 1
        subtree(tree[n][0])
        subtree(tree[n][1])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0]*2 for _ in range(E+2)]
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)//2):
        if tree[tmp[2*i]][0] == 0:
            tree[tmp[2*i]][0] = tmp[2*i+1]
        else:
            tree[tmp[2*i]][1] = tmp[2*i+1]
    # print(tree)

    cnt = 0
    subtree(N)

    print('#{} {}'.format(tc, cnt))