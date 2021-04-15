import sys; sys.stdin = open('sample_input.txt', 'r')



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global result
    Q = [(r, c)]
    tmp = ''
    tmp += arr[r][c]
    cnt = 0

    while Q and cnt < 6:
        cur_r, cur_c = Q.pop(0)
        cnt += 1
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # if 0 > nr or nc >= N or 0 > nc or nc >= N: continue
            if 0 <= nr < N and 0 <= nc < N:
                tmp += arr[nr][nc]
                Q.append((nr, nc))
                if len(tmp) == 7:
                    result.add(tmp) 
               
                   

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(input().split()) for _ in range(N)]
    result = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)   # i, j : 시작점
            
    print(result, len(result))
