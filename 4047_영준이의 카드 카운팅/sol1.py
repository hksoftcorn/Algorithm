import sys

sys.stdin = open('sample_input.txt', 'r')


def solution(c):
    cards = c
    S_deck = [1] * 13
    D_deck = [1] * 13
    H_deck = [1] * 13
    C_deck = [1] * 13

    result = []
    for i in range(len(cards) // 3):
        card = cards[3 * i: 3 * i + 3]
        shape = card[0]
        number = int(card[1:])

        if shape == 'S':
            S_deck[number - 1] -= 1

        elif shape == 'D':
            D_deck[number - 1] -= 1

        elif shape == 'H':
            H_deck[number - 1] -= 1

        elif shape == 'C':
            C_deck[number - 1] -= 1

        if S_deck[number - 1] == -1 or D_deck[number - 1] == -1 or H_deck[number - 1] == -1 or C_deck[number - 1] == -1:
            return 'ERROR'

    result += [sum(S_deck)]
    result += [sum(D_deck)]
    result += [sum(H_deck)]
    result += [sum(C_deck)]

    return ' '.join(map(str, result))


T = int(input())

for tc in range(1, T+1):
    cards = input()
    print('#{} {}'.format(tc, solution(cards)))






