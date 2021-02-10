import sys

sys.stdin = open('./s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = {}
    B_length = []

    for n in range(N):
        A, B = list(map(int, input().split()))
        tmp = [1] * B
        B_length.append(B)

        if A > 1:
            for a in range(A-1):
                tmp[a] = 0

        result[n] = tmp


    max_length = max(B_length)
    for key, value in result.items():
        result[key] = value + [0]*(max_length - len(value))

    bus_count = [0] * max_length
    for value in result.values():
        for idx in range(max_length):
            bus_count[idx] += value[idx]

    P = int(input())
    count = []
    for p in range(P):
        num = int(input())
        count.append(bus_count[num-1])

    print('#{} {}'.format(tc, " ".join([str(x) for x in count])))
