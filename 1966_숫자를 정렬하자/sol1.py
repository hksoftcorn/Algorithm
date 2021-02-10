import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    length = int(input())
    numbers = list(map(int, input().split()))

    for i in range(1, length):
        for j in range(0, length-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print('#{} {}'.format(tc, ' '.join([str(x) for x in numbers])))