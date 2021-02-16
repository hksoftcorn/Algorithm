import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, T = map(int, input().split())
    arr = [i for i in range(1, 13)]
    result = 0

    for i in range(1<<N):
        



    print('#{} {}'.format(tc, result))