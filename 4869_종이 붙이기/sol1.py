import sys
sys.stdin = open('sample_input.txt', 'r')


def solution(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3

    return solution(N-1) + 2*solution(N-2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, solution(N//10)))