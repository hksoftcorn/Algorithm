import sys; sys.stdin = open('input.txt', 'r')

def solution(c):
    global max_num
    if not c:   # count 횟수가 남지 않았으면
        tmp = int(''.join(arr))
        if max_num < tmp:
            max_num = tmp
        return
    else:
        for i in range(0, n-1):
            for j in range(i + 1, n):
                arr[i], arr[j] = arr[j], arr[i]
                tmp = int(''.join(arr))
                if not visited.get((tmp, c)):
                    visited[(tmp, c)] = True
                    solution(c - 1)
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for tc in range(1, T+1):
    N, C = input().split()  # N: 숫자판, C: 자리 바꿈 횟수
    arr = list(N)

    n = len(arr)
    c = int(C)

    visited = {}
    max_num = 0
    solution(c)
    
    print('#{} {}'.format(tc, max_num))


