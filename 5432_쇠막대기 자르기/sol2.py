import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):

    iron_bar = input()

    cnt = 0
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            cnt += 1
        else:
            cnt -= 1

            if iron_bar[i -1] == '(':
                ans += cnt
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))