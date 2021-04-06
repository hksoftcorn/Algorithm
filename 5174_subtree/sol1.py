import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    edge = list(map(int, input().split())) # p, c

    left = [0] * (V + 1)
    right = [0] * (V + 1)

    pa = [0] * (V + 1)

    for i in range(E):
        n1, n2 = edge[i * 2], edge[i * 2 + 1]  # n1 부모노드, n2 자식노드
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2
        pa[n2] = n1

    cnt = 0


    def solution(n):
        global cnt
        if n == 0:
            return
        else:
            cnt += 1
            solution(left[n])
            solution(right[n])


    solution(N)
    print('#{} {}'.format(tc, cnt))


