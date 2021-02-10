import sys
sys.stdin = open('input.txt')


T = 10

def solution(dump_limit, boxes):

    for _ in range(len(dump_limit)):
        max_idx = min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        diff = boxes[max_idx] - boxes[min_idx]
        if diff == 0:
            return 0
        elif diff ==1:
            return 1

    max_idx = min_idx = 0
    for idx in range(len(boxes)):
        if boxes[idx] > boxes[max_idx]:
            max_idx = idx
        elif boxes[idx] < boxes[min_idx]:
            min_idx = idx

    diff = boxes[max_idx] - boxes[min_idx]
    return diff



for tc in range(1, T+1):
    dump_limit = int(input())
    boxes = list(map(int, input().split()))

    print('#{} {}'.format(tc, solution(dump_limit, boxes)))
