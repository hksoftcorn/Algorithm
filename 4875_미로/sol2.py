import sys
sys.stdin = open('sample_input.txt')


def solution():
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == '2':
                S = (row, col)
            elif arr[row][col] == '3':
                G = (row, col)

    visited = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    current = S

    while current != G:




    def dfs(v):
        visited[v] = True
        for new_v in graph[v]:
            if not visited[new_v]:
                dfs(new_v)

    dfs(S)
    return int(visited[G])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    for idx in range(N):
        arr[idx] = ['*'] + list(input()) + ['*']
    arr = [['*']*len(arr[0])] + arr + [['*']*len(arr[0])]
    print(arr)

