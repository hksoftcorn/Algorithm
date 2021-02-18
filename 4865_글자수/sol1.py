import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()

    length_N = len(N)
    length_M = len(M)

    result = 0
    for i in range(length_M - length_N + 1):
        if M[i:i+length_N] == N:
            result = 1

    print('#{} {}'.format(tc, result))