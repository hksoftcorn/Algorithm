import sys
sys.stdin = open('input.txt', 'r')


def solution():
    global cnt

    first = bits[0]
    if first == '1':
        cnt += 1

    for idx in range(1, len(bits)):
        if bits[idx-1] != bits[idx]:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    bits = list(input())
    cnt = 0
    print('#{} {}'.format(tc, solution()))

