# Runtime Error
# Hmm,, how can i fix it ?
operations = [1, -1, -10, 2]
def bfs(n):
    global distance
    Q = [n]
    visited = [0] * 1000000
    visited[n] = 1

    while Q:
        cur_n = Q.pop(0)
        if cur_n == M:
            return
        for i in range(4):
            if i == 3:
                next_n = cur_n * operations[i]
            else:
                next_n = cur_n + operations[i]
            if next_n < 0 or next_n >= 1000000: continue
            if not visited[next_n]:
                visited[next_n] = 1
                distance[next_n] = distance[cur_n] + 1
                # if next_n == M:
                #     return
                Q.append(next_n)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    distance = [0] * 1000000
    bfs(N)
    print('#{} {}'.format(tc, distance[M]))
