import sys
sys.stdin = open('input.txt', 'r')


def solution(node_no):
    global tree
    if node_no == 1:
        return
    if tree[node_no // 2][2] > tree[node_no][2]:
        tree[node_no // 2][2], tree[node_no][2] = tree[node_no][2], tree[node_no // 2][2]
        solution(node_no // 2)


T = int(input())

for tc in range(1, T + 1):
    V = int(input())
    tree = [[0] * 3 for _ in range(V + 1)]
    input_data = list(map(int, input().split()))  # 서로 다른 자연수

    for node_no, node_data in enumerate(input_data, start=1):
        tree[node_no][2] = node_data  # 현재 들어온 데이터
        solution(node_no)

    ans = 0
    while V > 1:
        V //= 2
        ans += tree[V][2]

    print('#{} {}'.format(tc, ans))
