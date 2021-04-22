"""
MST 최소신장트리

문제 설명 : 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만드는 최소신장트리를 구하시오
컨셉 : Prim's Algorithm
"""
T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # V(Vertex): 정점은 0번부터 V까지, E(Edge): 간선의 수
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    
    MST = [0] * (V + 1)
    key = [0xfffffff] * (V + 1)
    key[0] = 0
    ans = 0
    
    for _ in range(V + 1): # 0 ~ V 까지 모든 정점을 돌아봅니다.
        u, min_key = 0, 0xfffffff   # 값을 초기화 합니다.
        for i in range(V + 1):
            if not MST[i] and min_key > key[i]:
                u, min_key = i, key[i]
        MST[u] = 1
        ans += key[u]

        for v, w in G[u]:
            if not MST[v] and key[v] > w:
                key[v] = w

    print('#{} {}'.format(tc, ans))




