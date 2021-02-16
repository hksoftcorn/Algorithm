import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 인덱스 함수 구현
    end_idx = arr[-1].index(2)
    y = 99
    x = end_idx

    

    # while y:
    #     if x == 0:
    #         if arr[x+1][y] == 1:
    #             x += 1
    #         else:
    #             y -= 1
    #     elif x == 99:
    #         if arr[x-1][y] == 1:
    #             x -= 1
    #         else:
    #             y -= 1
    #
    #     else:
    #         if arr[x-1][y] == 1:
    #             x -= 1
    #         elif arr[x+1][y] == 1:
    #             x += 1
    #         else:
    #             y -= 1

    print('#{} {}'.format(tc, x))



