import sys
sys.stdin = open('./sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    chargers = list(map(int, input().split()))

    start_point = 0
    end_point = 0

    count = 0

    while end_point < N:

        for number in range(start_point + K, start_point, -1):
            if number in chargers:
                start_point = number
                count += 1
                break
        if start_point == number-1:
            count=0
            break

        end_point = start_point + K


    print('#{} {}'.format(tc, count))