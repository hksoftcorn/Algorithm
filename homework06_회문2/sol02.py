
def solution(s):
    N = len(s)

    result = []
    # 가로 - 인덱스 슬라이싱
    for i in range(N):
        for left in range(N-1):
            for right in range(N-1, left, -1):
                palindrome = s[i][left:right+1]
                if palindrome == palindrome[::-1]:
                    result.append(palindrome)
                    break

    # 세로 - 인덱스 요소 접근
    for j in range(N):
        for top in range(N-1):
            for bottom in range(N-1, top, -1):
                palindrome = ''
                for m in range(top, bottom+1):
                    palindrome += s[m][j]

                if palindrome == palindrome[::-1]:
                    result.append(palindrome)

    # result 최고길이 반환
    max_length = 0
    for palin in result:
        if max_length < len(palin):
            max_length = len(palin)

    return max_length