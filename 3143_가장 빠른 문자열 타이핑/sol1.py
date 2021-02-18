import sys
sys.stdin = open('sample_input.txt')


def solution(N, M):
    count = 0
    while 1:
        if M in N:
            count += 1
            # replace 함수 구현
            N = N.replace(M, "", 1)
        else:
            break

    return len(N) + count


T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    print('#{} {}'.format(tc, solution(N, M)))