import sys

sys.stdin = open('./sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    input_data = list(map(int, input().split()))
    n = input_data[0]
    m = input_data[1]

    numbers = list(map(int, input().split()))
    max_num = sum(numbers[0:m])
    min_num = sum(numbers[0:m])

    for idx in range(n - m + 1):
        tmp = sum(numbers[idx:idx+m])
        if tmp > max_num:
            max_num = tmp

        elif tmp < min_num:
            min_num = tmp

        else:
            continue

    print('#{} {}'.format(tc, max_num - min_num))

