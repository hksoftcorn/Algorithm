import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    l = 1
    r = P
    c = int((l+r)/2)
    Acount = 0
    while c != Pa:
        if Pa > c:
            l = c
        else:
            r = c

        c = int((l + r) / 2)
        Acount += 1

    l = 1
    r = P
    c = int((l + r) / 2)
    Bcount = 0
    while c != Pb:
        if Pb > c:
            l = c
        else:
            r = c

        c = int((l + r) / 2)
        Bcount += 1

    if Acount == Bcount:
        print('#{} {}'.format(tc, 0))
    elif Acount < Bcount:
        print('#{} {}'.format(tc, 'A'))
    else:
        print('#{} {}'.format(tc, 'B'))



