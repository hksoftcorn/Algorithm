def dfs(v):
    global cnt
    if not v:
        pass


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        p, c = map(int, input().split())
        G[p].append(c)
        G[c].append(p)
    print(G)
