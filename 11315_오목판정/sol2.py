import sys
sys.stdin = open('11315_오목판정/sample_input.txt', 'r')


def check(matrix,N):
    for y in range(N):
        for x in range(N):
            if matrix[y][x] != 'o':
                continue
            # 우측 
            if x + 4 < N and solution(matrix, y, x, 0, 1): # solution(matrix, cy, cx, dy, dx)
                return 'YES'
            # 하단 
            if y + 4 < N and solution(matrix, y, x, 1, 0):
                return 'YES'
            # 좌측상단
            if x - 4 >= 0 and y - 4 >= 0 and solution(matrix, y, x, -1, -1):
                return 'YES'
            # 우측상단
            if x + 4 < N and y - 4 >= 0 and solution(matrix, y, x, -1, 1):
                return 'YES'
    return 'NO'
 
 
def solution(matrix, cy, cx, dy, dx):
    for z in range(1, 5):
        if matrix[cy + z*dy][cx + z*dx] != 'o':
            return False
    return True
 
 
 
test_case = int(input())
for i in range(1, test_case+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
 
    result = check(matrix,N)
    print("#{} {}".format(i, result))