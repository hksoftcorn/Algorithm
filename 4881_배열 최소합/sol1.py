import sys
sys.stdin = open('sample_input.txt', 'r')


def solution():




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, solution()))
