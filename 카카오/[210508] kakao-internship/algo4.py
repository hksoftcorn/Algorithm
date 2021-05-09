
def bfs(n, start, end, evenG, oddG, traps):
    visited = [0] * (n + 1)
    Q = [start]
    visited[start] = 1
    # dist = [0xffff] * (n + 1)
    # path = [[] for _ in range(n+1)]
    # path[start].append(start)
    trap_cnt = [0] * (n + 1)
    total_cost = [0xffff] * (n + 1)
    total_cost[start] = 0

    while Q:
        cur_n = Q.pop(0)

        # end를 만나면 끝
        if cur_n == end:
            # print(1)
            return total_cost[end]

        if cur_n in traps:
            trap_cnt[cur_n] += 1

        graph = oddG if trap_cnt[cur_n] % 2 else evenG
        for nodes in graph[cur_n]:
            visited[nodes[0]] = 0

        for w in graph[cur_n]:
            if not visited[w[0]]:
                visited[w[0]] = 1
                total_cost[w[0]] = total_cost[cur_n] + w[1]
                    # total_cost[w[0]] = total_cost[cur_n] + w[1]
                Q.append(w[0])


def solution(n, start, end, roads, traps):

    oddG = [[] for _ in range(n + 1)]
    evenG = [[] for _ in range(n + 1)]

    for road in roads:
        v, u, cost = road
        evenG[v].append((u, cost))

        if v in traps:
            oddG[u].append((v, cost))
        elif u in traps:
            oddG[u].append((v, cost))
        else:
            oddG[v].append((u, cost))

    # G.sorted(key=lambda x: (x[0], x[1]))
    answer = bfs(n, start, end, evenG, oddG, traps)
    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
result = 4

n = 3
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
solution(n, start, end, roads, traps)
