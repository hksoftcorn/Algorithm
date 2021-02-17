import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    print(arr)
    print(len(arr), len(arr[-1]))

    # 인덱스 함수 구현
    end_idx = arr[-1].index(2)
    print(end_idx)
    x = len(arr) - 2
    y = end_idx

    while x:
        if arr[x][y-1] == 1:
            y -= 1
        elif arr[x][y+1] == 1:
            y += 1
        else:
            x -= 1

    print('#{} {}'.format(tc, y-1))
