import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    length = int(input())
    blocks = list(map(int, input().split()))

    max_block = max(blocks)

    max_count = blocks.count(max_block)
    first_idx = blocks.index(max_block)
    count = length - max_count - first_idx

    ##아아아

    for idx, block in enumerate(blocks[:-1]): # 1, 0, 0, 0, 0, 0, 0, 7, 7
        for idx2, block2 in enumerate(blocks[idx+1:]):
            distance = 0
            if block <= block2:
                distance = idx2
                # idx+idx2+1
                tmp = len([i for i in blocks[idx+idx2+1:] if i == 0])
                tmp_count = distance + tmp

    if tmp_count > count:
        count = tmp_count


    print('#{} {}'.format(tc, count))