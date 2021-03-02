import sys
sys.stdin = open('input.txt', 'r')


operator = ('*', '+', '(', ')')


def is_number(x):
    if x not in operator:
        return True
    else:
        return False


def make_postfix(input_data):
    stack = []
    result = []

    def pref(x):
        if x == '*':
            return 2
        elif x == '+':
            return 1
        elif x == '(':
            return 0

    for data in input_data:
        # 피연산자(숫자)는 result에 넣어줍니다.
        if is_number(data):
            result.append(data)
        # 연산자라면 stack에 넣어서 우선순위를 판별합니다.
        elif data in operator:
            if data == ')':
                while len(stack) >  and stack[-1] != '(':
                    op = stack.pop()
                    result.append(op)
                stack.pop()
            else:
                p = pref(data)
                while len(stack):
                    top = stack[-1]
                    # 우선순위가 높은 연산자는 stack에 쌓일 자격이 있습니다
                    if pref(top) < p:
                        break
                    # 하지만 낮거나 같다면 pop되어야 하죠
                    else:
                        result.append(stack.pop())
                stack.append(data)

    return ''.join(result)


def solution(input_data):
    stack = []
    postfix_data = make_postfix(input_data)
    for p in postfix_data:
        if is_number(p):
            stack.append(int(p))
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

