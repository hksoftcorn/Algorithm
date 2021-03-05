import sys
sys.stdin = open('sample_input.txt', 'r')


# 백트래킹을 이용해 봅시다.
def perm(idx, sub_sum):
    global ans
    # 유망성 검사 // 가지치기
    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0
            st = sel[0]
            st2 = st + sel[1]

            # 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1
            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt +=1
            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1
            if ans > cnt:
                ans = cnt
                
        return

    for i in range(1, N - 1):
        sel[idx] = i
        perm(idx + 1, sub_sum + i)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 행, M : 열
    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3
    ans = 987654231

    # 앞에는 idx, 뒤에는 중간 합
    perm(0, 0)

    print('#{} {}'.format(tc, ans))
