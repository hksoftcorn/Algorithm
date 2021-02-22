import sys
sys.stdin = open('sample_input.txt', 'r')


def solution(string):
    result = 1
    stack = []
    openers = '({['
    closer = ')}]'

    for char in string:
        if char in openers:
            stack.append(char)

        if char in closer:
            if not len(stack):
                result = 0
                break
        else:
            if char == ')' and stack.pop() != '(':
                result = 0
                break
            elif char == '}' and stack.pop() != '{':
                result = 0
                break
            elif char == ']' and stack.pop() != '[':
                result = 0
                break
    else:
        if len(stack):
            result = 0

    return result


T = int(input())

for tc in range(1, T+1):
    input_data = input()
    print('#{} {}'.format(tc, solution(input_data)))
