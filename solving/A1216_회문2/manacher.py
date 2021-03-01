import sys
from datetime import datetime
sys.stdin = open('a_test.txt')

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    N = len(s)
    cnt_list = [0] * N

    """
    r: 지금까지 확인한 회문들의 가장 먼 우측 idx (대척점-mirror 용)
    p: 지금까지 확인한 회문들중 가장 긴 회문의 idx (꽃길 판별 용)
    """
    r = p = 0
    for idx in range(N):
        if idx <= r:
            m_idx = 2 * p - idx

            # 남은 꽃길 길이만큼으로 갱신
            if cnt_list[m_idx] > r - idx:
                cnt_list[idx] = r - idx
            else:  # 대척점 내용으로 갱신
                cnt_list[idx] = cnt_list[m_idx]
        else:
            m_idx = 0
        """
        idx - cnt_list[idx] => 현 idx 기준으로 확보한 회문 좌측 끝
        idx + cnt_list[idx] => 현 idx 기준으로 확보한 회문 우측 끝
        idx - cnt_list[idx] - 1 => 미지의 왼쪽
        idx + cnt_list[idx] + 1 => 미지의 오른쪽
        """
        while idx - cnt_list[idx] - 1 >= 0 and idx + cnt_list[idx] + 1 < N and\
                s[idx - cnt_list[idx] - 1] == s[idx + cnt_list[idx] + 1]:
            cnt_list[idx] += 1

        if r < idx + cnt_list[idx]:
            r = idx + cnt_list[idx]
            p = idx

    return max(cnt_list)


T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    print(manacher(input()))
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))
















