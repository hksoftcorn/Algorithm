import sys
sys.stdin = open("input.txt")


def solution(full, part):
    lf, lp = len(full), len(part)

    idx = cnt = 0
    # 현재 인덱스부터 단어 끝까지의 길이 >=  부분의 길이
    while lp <= lf - idx:
        # 찾았으면 cnt++ && Jump idx
        if full[idx:idx + lp] == part:
            cnt += 1
            idx += lp
        # 아니면 1씩 진행
        else:
            idx += 1
    return lf - (cnt * lp) + cnt


T = int(input())
for tc in range(1, T+1):
    full, part = input().split()
    print("#{} {}".format(tc, solution(full, part)))
