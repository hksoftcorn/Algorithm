import sys
sys.stdin = open('input.txt', 'r')


def find_max_idx(arr):
    max_idx = 0
    max_price = 0
    for idx in range(len(arr)):
        if max_price < arr[idx]:
            max_idx = idx
    return max_idx

result = 0
def solution(prices):
    prices = prices
    max_idx = find_max_idx(prices)

    for idx in range(max_idx):
        global result
        result += prices[max_idx] - prices[idx]

    if not max_idx == len(prices):
        prices = prices[max_idx + 1:]
        solution(prices)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(prices)))