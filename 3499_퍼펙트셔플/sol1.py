import sys

sys.stdin = open('sample_input.txt')


def solution(deck):
    deck = deck
    result = ''
    if N % 2:
        # 홀수
        list1 = deck[:N // 2 + 1]
        list2 = deck[N // 2 + 1:]
        for i in range(N // 2):
            result += list1[i]
            result += ' '
            result += list2[i]
            result += ' '
        result += list1.pop()

    else:
        list1 = deck[:N // 2]
        list2 = deck[N // 2:]

        for i in range(N // 2):
            result += list1[i]
            result += ' '
            result += list2[i]
            result += ' '

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = input().split()
    print('#{} {}'.format(tc, solution(deck)))



