import sys
sys.stdin = open('input.txt')


# def solution(N ,M):
#     result = 1
#     while M:
#         result *= N
#         M -= 1
#     return result


def solution(N, M):
    if M == 1:
        return N
    if M % 2:
        result = solution(N, (M-1)//2)
        return result * result * N
    else:
        result = solution(N, M // 2)
        return result * result


T = 10

for _ in range(1, T+1):
    tc = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, solution(N, M)))

