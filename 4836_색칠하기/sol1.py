import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(0 for i in range(10)) for j in range(10)]

    boxes = int(input())
    for _ in range(boxes):

        x1, y1, x2, y2, color = map(int, input().split())

        for dx in range(x2-x1+1):
            for dy in range(y2-y1+1):
                x = x1 + dx
                y = y1 + dy
                arr[x][y] += color


    result = [element for ar in arr for element in ar]


    print('#{} {}'.format(tc, result.count(3)))




