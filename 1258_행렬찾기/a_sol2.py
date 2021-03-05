import sys
from pandas import DataFrame

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j

                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1
                ans.append([r - i, c - j])

                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0

    ans.sort(key=lambda x: (x[0] * x[1], x[0]))

    print('#{} {}'.format(tc, len(ans)), end=' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
    print()
