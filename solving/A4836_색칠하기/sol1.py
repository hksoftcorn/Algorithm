import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    cnt = 0
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for y_idx in range(y1, y2+1):
            for x_idx in range(x1, x2+1):
                matrix[y_idx][x_idx] += color
                if matrix[y_idx][x_idx] == 3:
                    cnt += 1


    # from pandas import DataFrame
    # print(DataFrame(matrix), end='\n{}-----------------------------\n'.format(cnt))