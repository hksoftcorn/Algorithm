import sys
sys.stdin = open('input.txt', 'r')


def find_max_idx(arr):
    max_idx = 0
    max_price = 0
    for idx in range(len(arr)):
        if max_price < arr[idx]:
            max_idx = idx


def solution(prices):
    prices = prices
    max_idx = find_max_idx(prices)

    result = 0
    if max_idx:
        for idx in range(max_idx):
            result += prices[idx] - prices[idx]
    else:
        pass

    if not max_idx == len(prices)-1:
        post_prices = prices[max_idx+1:]
        arr = [0] * len(post_prices)

         


    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(prices)))

