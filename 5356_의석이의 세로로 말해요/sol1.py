import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    word = [0] * 5

    # 최대 길이
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        if len(word[i]) > max_len:
            max_len = len(word[i])

    # 세로로 읽기

    print('#{}'.format(tc), end=" ")
    for i in range(max_len):
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end='')
            # try:
            #     print(word[j][i], end='')
            # except:
            #     pass

