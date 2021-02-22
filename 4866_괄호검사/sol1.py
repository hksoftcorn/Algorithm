import sys
sys.stdin = open('sample_input.txt', 'r')


def solution():
    my_list = []

    for s in input_data:
        if s == '(' or s == '{':
            my_list.append(s)

        elif s == ')' or s == '}':
            if len(my_list):
                element = my_list.pop()
                if (s == ')' and element == '{') or (s == '}' and element == '('):
                    return 0
            else:
                return 0
    if len(my_list):
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    input_data = input()
    print('#{} {}'.format(tc, solution()))
