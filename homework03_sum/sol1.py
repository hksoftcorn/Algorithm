import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = []
    result = []

    for _ in range(100):
        arr.append(list(map(int, input().split())))

    for r in range(100):
        tmp = 0
        for c in range(100):
            tmp += arr[r][c]
        result.append(tmp)

    for c in range(100):
        tmp = 0
        for r in range(100):
            tmp += arr[r][c]
        result.append(tmp)

    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    result.append(tmp)

    tmp = 0
    for i in range(100):
        tmp += arr[i][100-1-i]
    result.append(tmp)

    max_number = result[0]
    for idx in range(len(result)):
        if max_number < result[idx]:
            max_number = result[idx]

    print('#{} {}'.format(tc, max_number))

