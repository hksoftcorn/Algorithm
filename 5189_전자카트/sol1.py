import sys; sys.stdin = open('sample_input.txt', 'r')

def dist(pos):
    cnt = 0
    for i in range(1, N + 1):
        r = pos[i-1]
        c = pos[i]
        cnt += arr[r][c]
    return cnt


def perm(k):
    global min_dist
    if k == N:
        # print(pos)
        tmp = dist(pos)
        if min_dist > tmp:
            min_dist = tmp
    else:
        for i in range(k, N):
            pos[k], pos[i] = pos[i], pos[k]
            perm(k + 1)
            pos[k], pos[i] = pos[i], pos[k]
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pos = list(range(N)) + [0]
    # print(arr, pos)
    min_dist = 0xfffff
    perm(1)

    print('#{} {}'.format(tc, min_dist))