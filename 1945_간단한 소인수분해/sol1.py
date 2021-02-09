import sys
sys.stdin = open('./input.txt')


T = int(input())

for tc in range(1, T+1):
    number = int(input())
    my_list = [2, 3, 5, 7, 11]

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while 1:
        if number % 2 == 0:
            number /= 2
            a += 1

        elif number % 3 == 0:
            number /= 3
            b += 1

        elif number % 5 == 0:
            number /= 5
            c += 1

        elif number % 7 == 0:
            number /= 7
            d += 1

        elif number % 11 == 0:
            number /= 11
            e += 1
        else:
            break

    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))
