import sys
sys.stdin = open('sample_input.txt')


def solution(input_data):
    stack = []
    operation = ['+', '-', '*', '/']
    input_data = input_data

    for data in input_data:
        if data not in operation and data != '.':
            stack.append(int(data))

        elif data in operation:
            if len(stack) <= 1:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if data == '+':
                result = a + b
                stack.append(result)
            elif data == '-':
                result = a - b
                stack.append(result)
            elif data == '*':
                result = a * b
                stack.append(result)
            elif data == '/':
                result = a // b
                stack.append(result)

        elif data == '.':
            result = stack.pop()
            return result


T = int(input())
for tc in range(1, T+1):
    input_data = input().split()
    print('#{} {}'.format(tc, solution(input_data)))




