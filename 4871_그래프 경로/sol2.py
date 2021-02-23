import sys
sys.stdin = open('sample_input.txt', 'r')


def solution(V, E, graph, S, G):
    # index 통일! vertex == visited idx == graph idx
    visited = [False for _ in range(V + 1)]  # 0번 미사용
    to_visits = [S]
    path = []

    while to_visits:
        current = to_visits.pop()

        if not visited[current]:
            visited[current] = True
            path.append(current)
            for v in graph[current]:
                if not visited[v]:
                    to_visits.append(v)
            to_visits += graph[current]
    #print(path)
    return int(visited[G])


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # undirected
        # graph[end].append(start)

    S, G = map(int, input().split())
    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))