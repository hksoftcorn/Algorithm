import sys
sys.stdin = open('./sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    length = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
        else:
            continue

    print('#{} {}'.format(tc, max_num-min_num))