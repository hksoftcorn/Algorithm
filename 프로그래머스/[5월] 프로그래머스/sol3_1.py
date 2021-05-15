def solution(s):
    answer = []

    def move_(ss):
        idx111 = -1
        cnt = 0     # 110의 갯수
        ss = list(ss)
        idx = 0
        while idx < len(ss) - 2:
            if ss[idx] == '1' and ss[idx + 1] == '1':
                if ss[idx + 2] == '1': # 111이 등장하는 최초의 인덱스
                    if idx111 == -1:
                        idx111 = idx    
                else:   # 110 등장
                    ss = ss[idx + 2:]
                    idx -= 1
                    cnt += 1
            idx += 1
        print(ss)
        if idx111 == -1:
            ans = ss[:] + ['1', '1', '0'] * cnt
        else:
            ans = ss[:idx111] + ['1', '1', '0'] * cnt + ss[idx111:]
        return ans

    for ss in s:
        print(ss)
        print(move_(ss))

    return answer

solution(["1110","100111100","0111111010"])