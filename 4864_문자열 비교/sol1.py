import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()

    alphabet = list(set(N))
    my_dict = {}
    for m in M:
        if m in alphabet:
            my_dict[m] = my_dict.get(m, 0) + 1

    # max 함수 구현
    result = 0
    for value in my_dict.values():
        if result < value:
            result = value

    print('#{} {}'.format(tc, result))