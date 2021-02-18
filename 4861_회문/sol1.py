import sys
sys.stdin = open('sample_input.txt')


def solution(N, M, arr):
    # 가로
    for i in range(N):
        for j in range(N-M+1):
            palindrome = arr[i][j:j+M]
            if palindrome == palindrome[::-1]:
                return palindrome
    # 세로
    for j in range(N):
        for i in range(N-M+1):
            palindrome =''
            for m in range(M):
                palindrome += arr[i+m][j]
            #print(palindrome)
            if palindrome == palindrome[::-1]:
                return palindrome

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

    print('#{} {}'.format(tc, solution(N, M, arr)))

