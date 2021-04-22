import sys; sys.stdin = open('sample_input.txt', 'r')


def bfs(v):
    global dist
    Q = [v]
    # visited = [0] * (V + 1)
    # visited[v] = 1
    dist[v] = 0
    result = set()
    while Q:
        cur_n = Q.pop(0)
        if cur_n == V:
            result.add(dist[V])
        for next_n, w in G[cur_n]:
            if dist[next_n] > dist[cur_n] + w:
                dist[next_n] = dist[cur_n] + w
                Q.append(next_n)
    return min(result)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    
    dist = [0xffffff] * (V + 1)
    ans = bfs(0)
    print('#{} {}'.format(tc, ans))
