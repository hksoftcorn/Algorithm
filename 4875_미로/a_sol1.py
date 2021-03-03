import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt')



def dfs(x, y):
    global found

    visited[y][x] = True
    #print(DataFrame(visited))
    if arr[y][x] == '3':
        found = True
    else:
        dys = [-1, 1, 0, 0]
        dxs = [0, 0, -1, 1]
        for idx in range(4):
            # 상하좌우
            dy, dx = dys[idx], dxs[idx]
            # 1. 0 <= x + dx, y + dy < N  -> index out of range x
            if 0 <= x + dx < N and 0 <= y + dy < N:
                # 2. 벽이 아닌가
                if arr[y + dy][x + dx] != '1':
                    # 3. 방문 했는지?
                    if not visited[y + dy][x + dx]:
                        dfs(x+dx, y+dy)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    for idx in range(N):
        arr[idx] = list(input())

    for y in range(N):
        for x in range(N):
            if arr[y][x] == '2':
                start = (x, y)
            elif arr[y][x] == '3':
                goal = (x, y)
    visited = [[False for _ in range(N)] for _ in range(N)]
    found = False
    dfs(*start)

    print('#{} {}'.format(tc, int(found)))

