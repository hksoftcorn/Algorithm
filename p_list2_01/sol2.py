import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    matrix = []
    matrix.append([0] * (N+2))
    for _ in range(N):
        matrix.append(
            [0, *map(int, input().split()), 0]
        )
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    result = 0

    for r in range(1, N+1):
        for c in range(1, N+1):
            for mode in range(4):
                center = matrix[c][r]
                testX = r + dx[mode]
                testY = c + dy[mode]
                around = matrix[testX][testY]

                if around:
                    result += abs(around - center)

    print("#{} {}".format(tc, result))