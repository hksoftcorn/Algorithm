import sys
sys.stdin = open('./sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    length = int(input())
    card_numbers = list(map(int, list(input())))

    result = {}
    for card in card_numbers:
        if card not in result:
            result[card] = result.get(card, 1)
        else:
            result[card] += 1


    max_num = 0
    for value in result.values():
        if value > max_num:
            max_num = value

    my_list = []
    for key, value in result.items():
        if value == max_num:
            my_list.append(key)

    print('#{} {} {}'.format(tc, max(my_list), max_num))



