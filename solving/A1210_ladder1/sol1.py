import sys
from pandas import DataFrame
sys.stdin = open("input.txt")

def solution(M):
    def show_matrix(M, x, y, nxt):
        if nxt == 'U':
            icon = '▲'
        elif nxt == 'R':
            icon = '>'
        elif nxt == 'L':
            icon = '<'
        M[y][x] = icon
        print(DataFrame(M), end='\n-------------------------\n')

    N = len(M)
    nxt = 'U'
    y = N - 1
    for x in range(N):
        last_row = M[y]
        if last_row[x] == 2:
            while y > 0:  # 올라갈 때는, 좌/우회전 우선
                if nxt == 'U':
                    if x < N - 1 and M[y][x+1]:  # 우회전
                        nxt = 'R'
                        x += 1
                    elif x > 0 and M[y][x-1]:  # 좌회전
                        nxt = 'L'
                        x -= 1
                    else:  # 직진
                        y -= 1
                else:  # 횡보중에는 올라가기 우선
                    if M[y-1][x]:
                        nxt = 'U'
                        y -= 1
                    elif nxt == 'R':
                        x += 1
                    elif nxt == 'L':
                        x -= 1
                # show_matrix(M, x, y, nxt)
            return x


T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    matrix = []
    for _ in range(N):
        matrix.append([n for n in map(int, input().split())])

    print("#{} {}".format(tc, solution(matrix)))

