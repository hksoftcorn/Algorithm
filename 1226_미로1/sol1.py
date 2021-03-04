import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y):
    global found

    visited[y][x] = True
    if matrix[y][x] == '3':
        found = True
    else:
        dys = [-1, 1, 0, 0]
        dxs = [0, 0, -1, 1]
        for idx in range(4):
            dy, dx = dys[idx], dxs[idx]
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if matrix[y + dy][x + dx] != '1':
                    # 3. 방문 했는지?
                    if not visited[y + dy][x + dx]:
                        dfs(x+dx, y+dy)

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    matrix = [list(input()) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '2':
                s = (x, y)
            if matrix[y][x] == '3':
                g = (x, y)

    visited = [[False for _ in range(N)] for _ in range(N)]
    found = False
    dfs(*s)
    print('#{} {}'.format(tc, int(found)))