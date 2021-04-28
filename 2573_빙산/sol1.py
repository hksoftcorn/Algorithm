N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    visited[r][c] = 1
    Q = [(r, c)]
    while Q:
        cur_r, cur_c = Q.pop()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] > 0:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))

def solution(matrix):
    global visited
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                if not visited[i][j]:
                    cnt += 1
                    dfs(i, j)
    if cnt > 2:
        return 1    # answer
    elif cnt == 0:
        return -1   # no answer
    else:
        return 0    # retry


year = 0
new_matrix = matrix[:]
while True:
    visited = [[0] * M for _ in range(N)]
    answer = solution(new_matrix)
    if answer == 1:
        break
    if answer == -1:
        year = 0
        break

    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] != 0:
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if 0 <= ni < N and 0 <= nj < M and new_matrix[i][j] > 0:
                        if new_matrix[ni][nj] == 0:
                            new_matrix[i][j] -= 1
    year += 1

print(year)