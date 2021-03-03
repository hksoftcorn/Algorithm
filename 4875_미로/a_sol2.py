import sys
from pandas import DataFrame

sys.stdin = open('sample_input.txt')


def dfs(x, y):
    global found

    # 이동하면 벽으로 만들어줘
    arr[y][x] = '1'

    if arr[y][x] == '3':
        found = True
    else:
        dys = [-1, 1, 0, 0]
        dxs = [0, 0, -1, 1]
        for idx in range(4):
            # 상하좌우
            dy, dx = dys[idx], dxs[idx]
            if 0 <= x + dx < N and 0 <= y + dy < N and arr[y + dy][x + dx] != '1':
                dfs(x + dx, y + dy)


T = int(input())
for tc in range(1, T + 1):
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

    found = False
    dfs(*start)

    print('#{} {}'.format(tc, int(found)))
