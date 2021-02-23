import sys
sys.stdin = open('sample_input.txt', 'r')


def solution():
    stack = []

    for s in string:
        # isEmpty
        if not len(stack):
            stack.append(s)
        # pop
        elif stack[-1] == s:
            stack.pop()
            continue
        # push
        else:
            stack.append(s)
    return len(stack)


T = int(input())

for tc in range(1, T + 1):
    string = input()
    print('#{} {}'.format(tc, solution()))