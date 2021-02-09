import sys
sys.stdin = open('./input.txt')


T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))


    for d in range(dump):
        top = boxes[0]
        top_idx = 0
        bottom = boxes[0]
        bottom_idx = 0

        for idx, element in enumerate(boxes):
            if element >= top:
                top = element
                top_idx = idx
            elif element <= bottom:
                bottom = element
                bottom_idx = idx
            else:
                continue

        if (top-bottom) <= 1:
            break

        boxes[top_idx] -= 1
        boxes[bottom_idx] += 1

    print('#{} {}'.format(tc, max(boxes) - min(boxes)))
