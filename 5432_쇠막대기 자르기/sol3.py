import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):

    iron_bar = input()

    s= []
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            s.append('(')
        else:
            s.pop()
            if iron_bar[i-1] == '(':
                ans += len(s)
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))


