# d(v) -> visitied[v] = True
# d(v)에서 인접한 v'에서 d(v') 실행

import sys
sys.stdin = open('sample_input.txt', 'r')


def solution(V, E, graph, S, G):
    # index 통일! vertex == visited idx == graph idx
    visited = [False for _ in range(V + 1)]  # 0번 미사용

    def dfs(v):
        visited[v] = True
        for new_v in graph[v]:
            if not visited[new_v]:
                dfs(new_v)

    dfs(S)
    return int(visited[G])


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())
    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))
