import sys
sys.stdin = open('input.txt')


def solution(N, arr):
    N = N
    arr = arr
    center = N//2
    result = 0

    for i in range(center):
        crop = arr[i][center - i : center + 1 + i]
        crop2 = arr[-(i+1)][center - i : center + 1 + i]
        for idx in range(len(crop)):
            result += int(crop[idx])
            result += int(crop2[idx])
    result += sum(map(int, arr[center]))
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        print('#{} {}'.format(tc, input()))
    else:
        arr = [list(input()) for _ in range(N)]
        print('#{} {}'.format(tc, solution(N, arr)))
