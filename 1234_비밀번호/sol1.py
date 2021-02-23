import sys
sys.stdin = open('input.txt', 'r')


def solution():
    stack = []

    for n in numbers:
        # isEmpty
        if not len(stack):
            stack.append(n)
        # pop
        elif stack[-1] == n:
            stack.pop()
            continue
        # push
        else:
            stack.append(n)
    return stack


T = 10

for tc in range(1, T + 1):
    _, numbers = list(map(str, input().split()))
    print('#{} {}'.format(tc, ''.join(solution())))