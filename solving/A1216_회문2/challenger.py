import sys
from datetime import datetime
sys.stdin = open('test.txt')


def solution(string):
    pass


T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    print(solution(input()))
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))


