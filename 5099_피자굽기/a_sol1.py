import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    pizza = list(map(int, input().split()))
    firepot = []

    for i in range(N):
        firepot.append((i+1, pizza[i]))

    # N번째 피자부터 넣어야함
    next_pizza = N

    while len(firepot) > 1:
        num, cheese = firepot.pop(0)
        cheese //= 2

        if cheese:
            firepot.append((num, cheese))
        else:
            if next_pizza < M:
                firepot.append((next_pizza+1, pizza[next_pizza]))
                next_pizza += 1

    print('#{} {}'.format(tc, firepot[0][0]))

