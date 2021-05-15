def solution(s):
    answer = []

    def moving_110(string):
        stack = []
        cnt = 0
        idx_111 = -1
        string = list(string)
        for idx in range(len(string)):
            ele = string[len(string) - 1 -idx]
            stack.append(ele)
            n = len(stack)
            if n <= 2: continue
            if stack[n-1] == '1' and stack[n-2] == '1' and stack[n-3] == '1':
                idx_111 = len(stack)
            if stack[n-1] == '1' and stack[n-2] == '1' and stack[n-3] == '0':
                cnt += 1
                stack.pop()
                stack.pop()
                stack.pop()
        
        if idx_111 == -1:
            stack = stack[::-1]
            tmp = 0
            while stack and stack[-1] != '0':
                stack.pop()
                tmp += 1
            ans = stack + ['1', '1', '0'] * cnt + ['1'] * tmp
            return ans
        else:
            ans = stack[:idx_111] + ['0', '1', '1'] * cnt + stack[idx_111:]
            return ans[::-1]


    for string in s:
        answer.append(''.join(moving_110(string)))

    return answer

print(solution(["1110","100111100","0111111010"]))
        # if len(stack) <= 2:
        #     ans = ['1', '1', '0'] * cnt + stack
        # else:
        #     stack = stack[::-1]
        #     tmp = 0
        #     for j in range(len(stack) - 2):
        #         if stack[j] == '1' and stack[j+1] == '1' and stack[j+2] == '1':
        #             tmp += 1
        #             break
        #     if tmp:
        #         ans = stack[:j] + ['1', '1', '0'] * cnt + stack[j:]
        #     else:
        #         ans = stack + ['1', '1', '0'] * cnt
        # return ans