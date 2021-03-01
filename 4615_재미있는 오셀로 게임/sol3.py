import sys
sys.stdin = open('sample_input.txt', 'r')

def check(col, row, color):
    global arr, N




def reversi(col, row, color):
    global arr
    # 상하좌우 / 대각선
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(8):
        d_x = dx[i]
        d_y = dy[i]
        change_list = []
        while True:




    arr[col][row] = color


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # 흑 : 1, 백 : 2
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2 - 1] = 2

    for _ in range(M):
        col, row, color = map(int, input().split())
        reversi(col, row, color)

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