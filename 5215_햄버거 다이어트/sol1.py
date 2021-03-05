import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())

    for _ in range(N):
        T, K = map(int, input().split()) # 맛 점수, 칼로리

