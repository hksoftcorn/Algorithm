import sys
sys.stdin = open('sample_input.txt')


def solution():
    visited = []
    stack = [start]
    while len(stack):
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return False if end in visited else True


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        start_node, end_node = map(int, input().split())
        graph[start_node] = graph.get(start_node, []) + [end_node]
    print(graph)
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, solution()))

    # print(start, end)
