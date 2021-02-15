import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    arr = []
    result = 0
    N = 5

    # 2차원 배열을 입력받는 방법
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 덽타를 이용한 2차 배열 탐색
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for r in range(N):
        for c in range(N):
            for mode in range(4):
                testX = r + dx[mode]
                testY = c + dy[mode]
                if 0 <= testX < N and 0 <= testY < N:
                    result += abs(arr[r][c] - arr[testX][testY])

    print("#{} {}".format(tc, result))







