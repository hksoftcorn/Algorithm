import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N : 2차원 크기 N x N
    # K : 내가 원하는 단어길이
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split()) for _ in range(N))]

    ans = 0

    for i in range(N):
        cnt = 0
        # 행 검사
        for j in range(N):
            if puzzle[i][j]:
                cnt += 1

            if puzzle[i][j] == 0 or j == N-1:
                # 벽을 만났을 시
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열 검사
        for j in range(N):
            if puzzle[j][i]:
                cnt += 1

            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(tc, ans))
