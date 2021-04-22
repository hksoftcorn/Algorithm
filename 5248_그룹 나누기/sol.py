def dfs(v):
    global visited
    visited[v] = 1
    
    for w in G[v]:
        if not visited[w]:
            dfs(w)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    input_data = list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for i in range(M):
        p, c = input_data[2 * i : 2 * (i + 1)]
        G[p].append(c)
        G[c].append(p)

    cnt = 0
    for idx in range(1, N + 1):
        if not visited[idx]:
            cnt += 1
            dfs(idx)
            
    print('#{} {}'.format(tc, cnt))
    