import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = []
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            # 사각형 내부의 합
            tmp = 0
            for dx in range(M):
                for dy in range(M):
                    tmp += arr[x + dx][y + dy]
            count.append(tmp)

    # max 함수 구현

    print('#{} {}'.format(tc, max(count)))
