import sys
sys.stdin = open('sample_input.txt')


def solution():
    def dfs(i, j):
        if i < 0 or i >= len(arr) or \
            j < 0 or j >= len(arr[0]) or \
            arr[i][j] != '0':
            return

        arr[i][j] = '#'
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)

    result = False
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '3':
                result = True
            elif arr[i][j] == '0':
                dfs(i, j)
    return int(result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    for idx in range(N):
        arr[idx] = list(input())
    print('#{} {}'.format(tc, solution()))

