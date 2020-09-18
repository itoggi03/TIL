import sys
sys.stdin = open("sample_input.txt", "r")

def bfs(start):
    Q.append(start)
    visited[start] = 1
    while Q:
        tmp = Q.pop(0)
        if tmp == G:
            return
        for idx in line[tmp]:
            if not visited[idx]:
                Q.append(idx)
                visited[idx] = visited[tmp] + 1

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    nod = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    line = [[] for _ in range(V+1)]

    for a,b in nod:
        line[a].append(b)
        line[b].append(a)

    Q = []
    visited = [0] * (V+1)
    bfs(S)
    print('#{} {}'.format(tc, visited[G]-1))