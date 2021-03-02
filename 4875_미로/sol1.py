import sys
sys.stdin = open('sample_input.txt')


def solution(arr, S, G):




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    for idx in range(N):
        arr[idx] = ['*'] + list(input()) + ['*']
        for idx2, num in enumerate(arr[idx]):
            if num == '2':
                S = (idx, idx2)
            if num == '3':
                G = (idx, idx2)

    print(arr, S, G)
    #print('#{} {}'.format(tc, solution()))
