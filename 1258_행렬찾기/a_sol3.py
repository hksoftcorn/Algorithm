import sys
from pandas import DataFrame

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sub_matrix = []

    for x in range(N):
        for y in range(N):
            if matrix[i][j]:
                lt = (x, y)
                dx = dy = 0
                while 0 <= x + dx + 1 < N and matrix[y][x + dx + 1]:
                    dx += 1
                while 0 <= y + dy + 1 < N and matrix[y + dy + 1][x]:
                    dy += 1
                rb = (x + dx, y + dy)
                sub_matrix.append((rb[1] - lt[1] + 1, rb[0] - lt[0] + 1))

                for ry in range(y, y + dy + 1):
                    for rx in range(x, x + dx + 1):
                        matrix[ry][rx] = 0

    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
    print()
