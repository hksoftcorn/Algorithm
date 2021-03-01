import sys
sys.stdin = open('sample_input.txt', 'r')


def check(arr, x, y, color):
    # 12시부터 8방향
    direction = [[0] * 3 for _ in range(3)]
    move = [-1, 0, 1]
    for dx in range(len(move)):
        for dy in range(len(move)):
            if move[dx] == 0 and move[dy] == 0:
                continue
            else:
                c = arr[x + move[dx]][y + move[dy]]
                if not c == 0 or c == color:
                    direction[dx][dy] = 1

    return direction


def reversi(arr, x, y, color):
    arr[x][y] = color
    # 8방향에서 자신과 다른 색상의 돌
    direction = check(arr, x, y, color)

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if direction[dx+1][dy+1] == 1:




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]
    # 흑 : 1, 백 : 2
    arr[N // 2][N // 2 + 1] = 1
    arr[N // 2 + 1][N // 2] = 1
    arr[N // 2][N // 2] = 2
    arr[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):
        y, x, color = map(int, input().split())
        arr = reversi(arr, x, y, color)

    print(arr)
    black = 0
    white = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))
