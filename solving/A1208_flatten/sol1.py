import sys
sys.stdin = open("input.txt")


def solution(dump_limit, boxes):
    for _ in range(dump_limit):
        max_idx = min_idx = 0
        # 가장 큰/작은 박스 찾기
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # dump 한 회차가 끝나고 확인하자
        max_idx = min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        diff = boxes[max_idx] - boxes[min_idx]
        if diff == 0:
            return 0
        elif diff == 1:
            return 1

    # dump limit 만큼 종료 (다시 찾을 필요 없음 by 김준형)
    return diff


T = 10
for tc in range(1, T+1):
    dump_limit = int(input())
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(dump_limit, boxes)))