import sys
sys.stdin = open('sample_input.txt')


def solution(N, omok):
    N = N
    omok = omok

    for i in range(N):
        # 가로
        for j in range(N-4):
            for t in range(5):
                if omok[i][j+t] == '.':
                    break
                if t == 4 and omok[i][j+t] == 'o':
                    return 'YES'
        # 세로
        for j in range(N-4):
            for t in range(5):
                if omok[j+t][i] == '.':
                    break
                if t == 4 and omok[i][j+t] == 'o':
                    return 'YES'

    for i in range(N-4):
        # 우하향
        for j in range(N-4):
            for t in range(5):
                if omok[i+t][j+t] == '.':
                    break
                if t == 4 and [i+t][j+t] == 'o':
                    return 'YES'
        # 좌하향
        for j in range(N-4):
            for t in range(5):
                if omok[i+t][(N-1) - (j+t)] == '.':
                    break
                if t == 4 and omok[i+t][(N-1) - (j+t)] == 'o':
                    return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    print('#{} {}'.format(tc, solution(N, omok)))



