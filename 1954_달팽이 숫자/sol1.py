import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(0 for i in range(N)) for j in range(N)]
    arr[0] = [i for i in range(1, N+1)]

    count = N-1
    r = 0
    c = count
    number = arr[r][c]  # N
    sign = 0
    while count != 0:
        for dr in range(count):
            # r 움직임
            r += (-1)**sign
            number += 1
            arr[r][c] = number

        for dc in range(count):
            c += (-1)**(sign+1)
            number += 1
            arr[r][c] = number

        sign += 1
        count -= 1

    print('#{}'.format(tc))
    for ar in arr:
        for element in ar:
            print(element, end=' ')
        print()























