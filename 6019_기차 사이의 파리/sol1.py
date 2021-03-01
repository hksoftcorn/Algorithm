import sys
sys.stdin = open('s_input.txt')


T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 시간 = 거리 / 속력
    hours = D / (A + B)
    result = F * hours
    print('#{} {}'.format(tc, result))
