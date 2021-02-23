import sys
sys.stdin = open('input.txt')


def solution():
    def factorial(k):
        if k == 0 or k == 1:
            return 1
        return k * factorial(k-1)

    def rev_factorial(n, k):
        count = 1
        if k == 0:
            return count
        else:
            for i in range(k):
                count *= (n - i -1)
        return count

    result = []
    for k in range(N):
        top = rev_factorial(N, k)
        bottom = factorial(k)
        tmp = int(top // bottom)
        result.append(tmp)

    return result


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print('#{}'.format(tc), end='')
    for N in range(n+1):
        print(' '.join(map(str, solution())))