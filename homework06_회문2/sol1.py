import sys
sys.stdin = open('input.txt')


def solution(arr):
    # 가로
    N = 100

    result = []
    for i in range(N):
        for left in range(N-1):
            for right in range(N-1, left, -1):
                palindrome = arr[i][left:right+1]
                if palindrome == palindrome[::-1]:
                    result.append(palindrome)
                    break
    # 세로
    for j in range(N):
        for top in range(N-1):
            for bottom in range(N-1, top, -1):
                palindrome =''
                for m in range(top, bottom+1):
                    palindrome += arr[m][j]

                if palindrome == palindrome[::-1]:
                    result.append(palindrome)

    max_length = 0
    for palin in result:
        if max_length < len(palin):
            max_length = len(palin)
    return max_length


T = 10

for _ in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, solution(arr)))