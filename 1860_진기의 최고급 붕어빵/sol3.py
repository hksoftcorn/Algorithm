import sys
sys.stdin = open('input.txt', 'r')


def solution():
    result = 'Possible'
    bread = 0
    for i in range(0, 12000, M):
        time_zone = list(range(i, i+M))
        cnt = 0
        for t in T:
            if t in time_zone:
                cnt += 1

        if i == 0 and cnt > 0 :
            result = 'Impossible'

        if i > 0:
            bread += K - cnt
            if bread < 0 :
                result = 'Impossible'

    return result


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 방문 시간
    T = list(map(int, input().split()))
    T.sort()
    print('#{} {}'.format(tc, solution()))


