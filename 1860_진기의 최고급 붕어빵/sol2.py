import sys
sys.stdin = open('input.txt', 'r')


def solution():
    nothing = [i for i in range(M)]
    for t in T:
        if t in nothing:
            return 'Impossible'

    # 12,000초
    for idx in range(12000//M + 1):
        



T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 방문 시간
    T = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution()))


