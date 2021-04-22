import sys; sys.stdin = open('input.txt', 'r')

def prim():
    global ans
    MST = [False] * V
    key = [0xffffff] * V
    key[0] = 0

    for _ in range(V):
        # key 값이 최소인 정점 찾기
        u, min_key = 0, 0xfffffff
        for i in range(V):
            if not MST[i] and min_key > key[i]:
                u, min_key = i, key[i]

        # 트리에 포함된 정점으로 표시
        MST[u] = True
        ans += key[u]
        for v, w in G[u]:
            if not MST[v] and key[v] > w:
                key[v] = w


T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    xs = list(map(str, input().split()))
    ys = list(map(str, input().split()))
    TAX = float(input())  # 세율

    lands = []
    for x, y in zip(xs, ys):
        lands.append((x, y))
    
    G = [[] for _ in range(V)]

    for i in range(V - 1):
        cur_x, cur_y = lands[i]
        for j in range(i + 1, V):
            other_x, other_y = lands[j]
            cost = ((int(other_x) - int(cur_x)) ** 2 + (int(other_y) - int(cur_y)) ** 2) * TAX
            G[i].append((j, cost))
            G[j].append((i, cost))

    ans = 0
    prim()
    print('#{} {}'.format(tc, round(ans)))