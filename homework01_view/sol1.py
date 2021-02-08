import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    result = 0
    width = int(input())
    height = list(map(int, input().split()))

    for idx, element in enumerate(height):
        if idx < 2 or idx > (width-3):
            continue

        left_list = height[idx-2:idx]
        right_list = height[idx+1:idx+3]
        top = 0

        for l in left_list:
            if top < l:
                top = l
        for r in right_list:
            if top < r:
                top = r

        if top >= element:
            continue

        else:
            result += element - top

    print('#{} {}'.format(tc, result))











