import sys

sys.stdin = open('sample_input.txt', 'r')


def solution():
    def bfs():
        visited = [0 for _ in range(V + 1)]

        queue = [S]
        visited[S] = True

        while queue:
            current = queue.pop(0)

            if current == G:
                return visited[G] - 1

            for i in graph[current]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[current] + 1
        return 0
    return bfs()


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, solution()))
