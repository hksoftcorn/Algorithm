import sys
sys.stdin = open('input.txt', 'r')


def solution():
    def isSudoku(cnt):
        for i in cnt:
            if not i == 1:
                return False
        return True

    # 가로
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[arr[i][j] -1] += 1
        if isSudoku(cnt) == False:
            return False
    # 세로
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[arr[j][i] - 1] += 1
        if isSudoku(cnt) == False:
            return False
    # 3x3
    for col in range(0, 9, 3):
        for row in range(0, 9, 3):
            cnt = [0] * 9
            for i in range(3):
                for j in range(3):
                    cnt[arr[col+i][row+j]-1] += 1
            if isSudoku(cnt) == False:
                return False
    return True


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, int(solution())))
