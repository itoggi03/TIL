import sys
sys.stdin = open("input.txt")

def bfs(s):
    Q.append(s)
    visited[s] = 1
    while Q:
        temp = Q.pop(0)
        for i in line[temp]:
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[temp] + 1

for tc in range(1, 11):
    l, start = map(int, input().split())
    tmp = list(map(int, input().split()))
    nod = max(tmp)
    line = [[] for _ in range(nod+1)]
    visited = [0] * (nod+1)
    for i in range(len(tmp)//2):
        line[tmp[2*i]].append(tmp[2*i+1])

    # print(tree)

    Q = []
    bfs(start)

    # print(visited)
    max_cnt = 0
    result = 0
    for i in range(len(visited)-1, 0, -1):
        if visited[i] > max_cnt:
            max_cnt = visited[i]
            result = i

    print(result)