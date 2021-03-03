import sys
sys.stdin = open('input.txt', 'r')


def solution():
    my_list = list(range(1,6))
    cnt = 0
    while True:
        number = numbers.pop(0)
        new_number = number - my_list[cnt % 5]
        if new_number <= 0:
            numbers.append(0)
            break
        numbers.append(new_number)
        cnt += 1
    return numbers


T = 10
for _ in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, ' '.join(map(str, solution()))))