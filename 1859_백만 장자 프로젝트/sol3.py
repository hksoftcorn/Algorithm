import sys
sys.stdin = open('input.txt', 'r')


def solution():
    total = 0
    max_value = prices[-1]
    for i in range(len(prices)-1, -1, -1):
        if max_value > prices[i]:
            total += max_value - prices[i]
        else:
            max_value = prices[i]
    return total

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution()))