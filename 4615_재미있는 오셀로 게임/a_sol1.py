import sys
sys.stdin = open('input.txt', 'r')


def checker(y, x, color):
    board[y][x] = color

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            cy = y + dy
            dx = x + dx
            found = False
            while 0 <= cs < N and 0 <= cy < N:
                if board[cy][cs] == 3 - color:
                    cy += dy
                    cs += dx
                elif board[cy][cx] == color:
                    found = True
                    break
                else:
                    break

            if found:
                px, py = x + dx, y + dy
                while px != cs or py != cy:
                    board[py][px] = color
                    px += dx
                    py += dy



T = int(input())
for tc in range(1, T+1):
    N, turns = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]

    board[N//2-1][N//2] = board[N//2][N//2-1] = 1
    board[N // 2][N // 2] = board[N // 2 -1][N // 2 -1] = 1

    for _ in range(turns):
        x, y, color = map(int, input().split())
        checker(y-1, x-1, color)

    black =white = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                black += 1
            elif board[y][x] == 2:
                white += 1
            