import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt', 'r')


def solution():

    visited = [False for _ in range(V+1)]
    to_visited = [start]
    
    visited[start] = True

    distances = [0 for _ in range(V+1)]

    while to_visited:
        v = to_visited.pop(0)

        for new_v in G[v]:
            if not visited[new_v]:
                to_visited.append(new_v)
                visited[new_v] = True
                distances[new_v] = distances[v] + 1
            if new_v == goal:
                return distances[goal]
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V : 정점의 수 1번부터 시작, E : 노드 간 간선의 수
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split()) # 간선 정보
        G[v1].append(v2)
        G[v2].append(v1)

    start, goal = map(int, input().split())
    print('#{} {}'.format(tc, BFS(sV)))
