import sys
from pandas import DataFrame
sys.stdin = open('input.txt', 'r')

def solution():
    # 시작점은 상, 좌 = 0
    start_points = []
    end_points = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if matrix[i][j] != 0:
                if matrix[i - 1][j] == 0 and matrix[i][j - 1] == 0:
                    start_points.append((i, j))

    area = []
    result = []
    for idx in range(len(start_points)):
        s_r, s_c = start_points[idx]
        r_cnt = c_cnt = 0
        while 1:
            if matrix[s_r + r_cnt][s_c] == 0:
                break
            r_cnt += 1
        while 1:
            if matrix[s_r][s_c + c_cnt] == 0:
                break
            c_cnt += 1
        area.append((r_cnt + 1) * (c_cnt + 1))
        result.append((r_cnt, c_cnt))

    rresult = [len(start_points)]
    for _ in range(len(area)):
        min_idx = area.index(min(area))
        area.pop(min_idx)
        rresult.extend(result.pop(min_idx))

    return rresult


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * (N + 2)]
    matrix += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    matrix += [[0] * (N + 2)]
    # print(DataFrame(matrix))
    print('#{} {}'.format(tc, ' '.join(map(str, solution()))))
