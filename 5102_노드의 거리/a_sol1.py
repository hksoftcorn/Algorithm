import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt', 'r')


def BFS(sV):
    Q = [[sV, 0]]
    visited = [False] * (V+1)
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)

        # 현재 내가 서있는 위치가 도착지라면 dist 반환
        if v == eV:
            return dist

        for i in range(1, V+1):
            if arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist+1])
                visited[i] = True
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V : 정점의 수 1번부터 시작, E : 노드 간 간선의 수
    arr = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split()) # 간선 정보
        arr[v1][v2] = 1
        arr[v2][v1] = 1

    print(DataFrame(arr))
    sV, eV = map(int, input().split())
    print('#{} {}'.format(tc, BFS(sV)))
