import sys
sys.stdin = open('dfs_bfs_input.txt', 'r')


def solution():

    def dfs():
        visited = [False for _ in range(N+1)]
        to_visits = [V]
        path = []

        while to_visits:
            #to_visits.reverse()
            current = to_visits.pop()
            if not visited[current]:
                visited[current] = True
                path.append(current)
                to_visits += sorted(graph[current], reverse=True)

        return path

    def bfs():
        visited = [False for _ in range(N + 1)]
        to_visits = [V]
        path = []
        while to_visits:
            current = to_visits.pop(0)
            if not visited[current]:
                visited[current] = True
                path.append(current)

            for i in sorted(graph[current], reverse=False):
                if not visited[i]:
                    to_visits.append(i)
        return path

    return dfs(), bfs()






T = int(input())

for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)


    print('#{} {}'.format(tc, solution()))



