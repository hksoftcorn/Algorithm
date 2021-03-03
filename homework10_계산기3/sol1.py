import sys
sys.stdin = open('input.txt', 'r')


operator = ('*', '/', '+', '-', '(', ')')


def is_number(x):
    if x not in operator:
        return True
    else:
        return False


def make_postfix(input_data):
    stack = []
    result = []

    def pref(x):
        if x == '*' or x == '/':
            return 3
        elif x == '+' or x == '-':
            return 2
        elif x == '(':
            return 1

    for data in input_data:
        # 피연산자(숫자)는 result에 넣어줍니다.
        if is_number(data):
            result.append(data)
        # 연산자라면 stack에 넣어서 우선순위를 판별합니다.
        elif data == '(':
            stack.append(data)
        elif data == ')':
            while len(stack) > 0 or stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while len(stack) > 0 or pref(stack[-1]) >= pref(data):
                result.append(stack.pop())
            result.append(data)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


def solution(input_data):
    stack = []
    postfix_data = make_postfix(input_data)
    for p in postfix_data:
        if is_number(p):
            stack.append(int(p))
        elif len(stack) == 1:
            stack.append()

        else:
            post = stack.pop()
            pre = stack.pop()
            if p == '+':
                stack.append(pre + post)
            else:
                stack.append(pre * post)


    return sum(stack)


T = 10

for tc in range(1, T+1):
    N = int(input())
    input_data = input()
    print('#{} {}'.format(tc, make_postfix(input_data)))

