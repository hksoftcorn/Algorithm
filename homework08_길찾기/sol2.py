import sys
sys.stdin = open('input.txt')


def solution(graph):
    visited = [False for _ in range(100)]
    to_visits = [0]

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            to_visits += graph[current]

    return int(visited[99])


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    graph = [[] for _ in range(100)]
    edge_list = list(map(int, input().split()))
    for idx in range(0, len(edge_list), 2):
        graph[edge_list[idx]].append(edge_list[idx + 1])

    print('#{} {}'.format(tc, solution(graph)))

