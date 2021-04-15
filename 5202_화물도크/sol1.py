import sys; sys.stdin = open('sample_input.txt', 'r')

def solution(arr):
    global cnt
    start = -1
    for i in range(len(arr)):
        s, e = arr[i]
        if start <= s:
            cnt += 1
            start = e
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedules = []

    for _ in range(N):
        s, e = map(int, input().split())
        schedules.append((s, e))

    schedules.sort(key=lambda x: x[1])
    cnt = 0
    solution(schedules)
    print('#{} {}'.format(tc, cnt))