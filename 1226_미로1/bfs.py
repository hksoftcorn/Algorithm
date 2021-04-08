import sys
sys.stdin = open('input.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 리스트 큐
def BFS(r, c):
    Q = [(r, c)]
    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i] # nextRow+
            nc = cur_c + dc[i] # nextColumn

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if maze[nr][nc] == 3:
                return 1
            if maze[nr][nc] != 1:
                Q.append((nr, nc))
                maze[nr][nc] = 1
    return 0


T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i  # startRow
                sC = j  # startColumn
                maze[i][j] = 1

    print('#{} {}'.format(tc, BFS(sR, sC)))