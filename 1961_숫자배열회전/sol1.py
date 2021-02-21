import sys
sys.stdin = open('input.txt')


def solution(N, arr):
    N = N
    arr = arr
    result = [[0]*3 for _ in range(N)]

    # 90 / 180 / 270
    for i in range(N):
        tmp1 = ''
        tmp2 = ''
        tmp3 = ''
        for j in range(N):
            tmp1 += arr[N-1-j][i]
            tmp2 += arr[N - 1 - i][N - 1 - j]
            tmp3 += arr[j][N - 1 - i]
        result[i][0] = tmp1
        result[i][1] = tmp2
        result[i][2] = tmp3

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    result = solution(N, arr)
    print('#{}'.format(tc))
    for i in range(len(result)):
        print(*result[i])