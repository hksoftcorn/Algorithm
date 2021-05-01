N, M = map(int, input().split())
Queens = list(map(int, input().split()))
Knights = list(map(int, input().split()))
Pawns = list(map(int, input().split()))

visited = [[0] * M for _ in range(N)]

def move_knight(r, c):
    global visited
    dr = [-1, 1, -2, 2, -2, 2, -1, 1]
    dc = [2, 2, 1, 1, -1, -1, -2, -2]
    cur_r, cur_c = r, c
    for i in range(8):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            visited[nr][nc] = 1


def move_queen(r, c):
    global visited
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            cur_r, cur_c = r, c
            nr = cur_r + dr
            nc = cur_c + dc
            while 0 <= nr < N and 0 <= nc < M and (visited[nr][nc] == 0 or visited[nr][nc] == 1):
                visited[nr][nc] = 1
                nr += dr
                nc += dc


for i in range(1, len(Pawns), 2):
    pr, pc = Pawns[i : i + 2]
    visited[pr - 1][pc - 1] = 'p'

for j in range(1, len(Knights), 2):
    kr, kc = Knights[j : j + 2]
    visited[kr - 1][kc - 1] = 'k'
    move_knight(kr - 1, kc - 1)

for k in range(1, len(Queens), 2):
    qr, qc = Queens[k : k + 2]
    visited[qr - 1][qc - 1] = 'q'
    move_queen(qr - 1, qc - 1)

print(sum([x.count(0) for x in visited]))