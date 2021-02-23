import sys
sys.stdin = open('input.txt', 'r')


def solution():
    # 후위 연산
    stack = []
    for s in input_data:
        if not stack:
            stack.append(s)
        elif s != '+':
            stack.append(s)
        elif s == '+':
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            result = int(tmp1) + int(tmp2)
            stack.append(result)

    return stack



T = 10

for tc in range(1, T+1):
    N = int(input())
    input_data = input()
    # 후위 연산식 변환
    input_data = input_data[0] + input_data[2:] + input_data[1]
    print('#{} {}'.format(tc, *solution()))
