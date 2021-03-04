import sys
sys.stdin = open('sample_input.txt', 'r')


def playing_game(x, y):
    if students[x] == 1 and students[y] == 3:
        return x
    elif students[x] == 3 and students[y] == 1:
        return y
    elif students[x] >= students[y]:
        return x
    else:
        return y


def solution(start, end):
    if end - start == 0:
        return end

    elif end - start == 1:
        return playing_game(start, end)

    return playing_game(solution(start, (start+end)//2), solution((start+end)//2+1, end))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(0, N-1) + 1))