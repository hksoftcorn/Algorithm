N, M = map(int, input().split())

visited = [0] * 100001
queue = [0] * 100001
front = rear = -1

rear += 1
queue[rear] = N
visited[rear] = 1

while front != rear:
    front += 1
    n = queue[front]
    if n == M:
        print(visited[n])
    t = [n - 1, n + 1, 2 * n]
    for x in t:
        if 0 <= x <= 100000:
            if not visited[x]:
                visited[x] = visited[n] + 1
                rear += 1
                queue[rear] = x