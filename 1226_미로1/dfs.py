import sys
sys.stdin = open('input.txt', 'r')

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 리스트 큐
def DFS(r, c):
    global flag

    # 도착지점 확인
    if maze[r][c] == 3:
        flag = 1
        return

    maze[r][c] = 1
    for i in range(4):
        nr = r + dr[i]  # nextRow+
        nc = c + dc[i]  # nextColumn

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if maze[nr][nc] != 1:
            DFS(nr, nc)


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
    flag = 0
    DFS(sR, sC)

    print('#{} {}'.format(tc, flag))