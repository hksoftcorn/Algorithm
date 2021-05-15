def solution(numbers):
    answer = []
    def itob(i):
        ans = ''
        while i:
            ans = str(i % 2) + ans
            i //= 2 
        return ans


    def btoi(b):
        total = 0
        i = 0
        while i < len(b):
            total += int(b[len(b) - 1 - i]) * (2 ** i)
            i += 1

        return total


    def find_answer(number):
        odd_byte = list(itob(number))
        for idx in range(len(odd_byte)):
            if odd_byte[len(odd_byte) - 1 - idx] == '0':
                zero_idx = len(odd_byte) - 1 - idx
                odd_byte[zero_idx] = '1'
                while odd_byte[zero_idx + 1] != '1':
                    zero_idx += 1
                odd_byte[zero_idx + 1] = '0'
                return odd_byte
        else:
            odd_byte[0] = '0'
            odd_byte = ['1'] + odd_byte
            return odd_byte



    for number in numbers:
        if number % 2:
            bit_ans = find_answer(number)
            answer.append(btoi(bit_ans))
        else:
            answer.append(number + 1)

    return answer

print(solution([2,7]))



"""
좋은 풀이법
2개의 비트를 반전시키는 방법
+ 2 ** idx - 2 ** (idx - 1)
손병현.py
"""

def solution(numbers):
    ans = []

    for n in numbers:
        if n & 1:
            tmp, idx = n, 0
            while tmp > 0 and tmp % 2: 
                tmp//=2
                idx+=1
            ans.append(n + 2**idx - 2**(idx-1))
        else: ans.append(n+1)
    return ans