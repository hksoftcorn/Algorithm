import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A_numbers = list(map(int, input().split()))
    B_numbers = list(map(int, input().split()))

    result = []
    if N < M:
        for idx in range(M-N+1):
            tmp = 0
            for idx2 in range(N):
                tmp += A_numbers[idx2] * B_numbers[idx+idx2]
            result.append(tmp)

    else:
        for idx in range(N-M+1):
            tmp = 0
            for idx2 in range(M):
                tmp += B_numbers[idx2] * A_numbers[idx+idx2]
            result.append(tmp)

    max_result = result[0]
    for i in result:
        if max_result < i:
            max_result = i

    print('#{} {}'.format(tc, max_result))