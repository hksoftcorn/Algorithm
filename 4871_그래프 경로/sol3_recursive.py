import sys
sys.stdin = open('sample_input.txt', 'r')
# recursive


def solution(graph, S):
    to_visits = [S]
    if not len(to_visits):
        return
    else:
        current = to_visits.pop()
        visited[current] = True
        path.append(current)

        # for v in graph[current]:
        #     if not visited[v]:
        #         to_visits.append(v)
        #         return solution(graph, *to_visits)
        to_visits += graph[current]
        for s in to_visits:
            return solution(graph, s)


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
    visited = [False for _ in range(V + 1)]  # 0번 미사용
    path = []
    print('#{} {}'.format(tc, solution(graph, S)))
    print(path)

