import sys; sys.stdin = open('sample_input.txt', 'r')
"""
최소비용
문제 설명 : N x N Matrix에서 (0, 0)에서 출발하여 (N-1, N-1)까지 도달하는 최소 비용을 구하시오.
        (1) 이동마다 cost는  +1 / (2) 기입된 숫자는 높이를 말하며, 낮은 곳에서 높은 곳으로 이동 시에는 높이 차만큼의 cost가 붙음
컨셉 : Dijkstra Algorithm
"""

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(r, c):
    Q = [(r, c)]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dist[r][c] = 0
    
    while Q: # BFS 시작
        cur_r, cur_c = Q.pop(0)                                       # 자료구조 : 큐
        for i in range(4):                                            # 4방향을 돌아다닙니다.
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 > nr or nr >= N or 0 > nc or nc >= N: continue
            # if not visited[nr][nc]:   
            if arr[nr][nc] - arr[cur_r][cur_c] > 0:                   # 경사를 올라간다면 cost를 더해줍니다.
                cost = arr[nr][nc] - arr[cur_r][cur_c] + 1
            else:                                                     # 아니라면 그대로 +1
                cost = 1
            if dist[nr][nc] > dist[cur_r][cur_c] + cost:              # 다음지역과 현재지역 + cost를 비교합니다.
                dist[nr][nc] = dist[cur_r][cur_c] + cost
                visited[nr][nc] = 1
                Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = (0, 0)
    dist = [[0xfffffff] * N for _ in range(N)]
    bfs(*s)
    print('#{} {}'.format(tc, dist[N-1][N-1]))