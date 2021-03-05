import sys
from pandas import DataFrame
sys.stdin = open('input.txt', 'r')


def search_size(r, c):
    r_cnt = c_cnt = 0

    # 가로, 세로 길이 구하기
    for i in range(r, N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break

    for j in range(c, N):
        if arr[r][j] != 0:
            c_cnt += 1
        else:
            break

    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)


def init(r, c, r_cnt, c_cnt):
    for i in range(r, r+r_cnt):
        for j in range(c, c+c_cnt):
            arr[i][j] = 0


def counting_sort(idx):
    cnt = [0] * 10001
    sort_ans = [0] * len(ans)

    # 1. 카운팅
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    # 2. 누적합
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 3. 정렬하여 넣기
    for i in range(len(ans)-1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1

    return sort_ans


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                search_size(i, j)

    ans = counting_sort(0) # 행 우선 정렬
    ans = counting_sort(2) # 사각형 넓이로 정렬

    print('#{} {}'.format(tc, len(ans)), end=' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
    print()
