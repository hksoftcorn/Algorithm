import sys
sys.stdin = open('sample_input.txt', 'r')


def solution():
    global cnt

    # 첫 번째, 마지막 번째 줄
    for color in colors[0]:
        if color != 'W':
            cnt += 1
    for color in colors[N-1]:
        if color != 'R':
            cnt += 1

    for r in range(1, N-1):
        for c in range(M):
            colors[r][c]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    colors = [list(input()) for _ in range(N)]
    cnt = 0
    print('#{} {}'.format(tc, solution()))