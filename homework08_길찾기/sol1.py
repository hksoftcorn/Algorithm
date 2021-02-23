import sys
sys.stdin = open('input.txt')


def solution():
    S, G = 0, 99
    visited = [False for _ in range(100)]
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


T = 10
for _ in range(1, T+1):
    tc, l = map(int, input().split())
    graph = [[] for _ in range(100)]
    input_data = list(map(int, input().split()))
    for idx in range(l):
        graph[input_data[2 * idx]].append(input_data[2 * idx + 1])

    print('#{} {}'.format(tc, solution()))
