import sys; sys.stdin = open('sample_input.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(v):
    Q = [v]
    r, c = v
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    distance[r][c] = arr[r][c]
    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # if 0<= nr < N and 0 <= nc < N:
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            if not visited[nr][nc]:
                if distance[nr][nc] > distance[cur_r][cur_c] + arr[nr][nc]:
                    distance[nr][nc] = distance[cur_r][cur_c] + arr[nr][nc]
                    Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[0xfffff] * N for _ in range(N)]
    s = (0, 0)
    bfs(s)
    print('#{} {}'.format(tc, distance[N-1][N-1]))
    