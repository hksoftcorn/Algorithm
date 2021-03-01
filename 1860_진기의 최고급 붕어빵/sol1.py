import sys
sys.stdin = open('input.txt', 'r')


def solution():
    T.sort()

    bread = 0
    for idx in range(M, 12345, M):
        buyer = 0
        for t in T:
            if t >= (idx-M) and t < (idx):
                buyer += 1

        bread += K

        if buyer > bread:
            return 'Impossible'
        else:
            bread -= buyer

    return 'Possible'



T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 방문 시간
    T = list(map(int, input().split()))







