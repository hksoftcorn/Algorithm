import sys
sys.stdin = open('sample_input.txt', 'r')


def playing_game(left, right):
    x = left
    y = right
    if (x == 1 and y == 3) or x >= y:
        return x
    else:
        return y


def solution(numbers):
    if len(numbers) == 1:
        return numbers
    elif len(numbers) == 2:
        return playing_game(numbers[0], numbers[1])
    mid = len()





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(input().split())
    print(numbers)
    print('#{} {}'.format(tc, solution(numbers)))