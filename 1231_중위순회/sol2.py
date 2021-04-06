T = 10
for tc in range(1, T+1):
    V = int(input())

    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    for _ in range(V):
        input_data = input().split()
        node_no = int(input_data[0])
        node_data = input_data[1]

        tree[node_no][2] = node_data
        ans = []

        # node_no * 2 가 마지막 노드번호(V)보다 작다 == 왼쪽 자식이 있다.
        if node_no * 2 <= V:
            tree[node_no][0] = int(input_data[2])
            # node_no * 2 + 1 가 마지막 노드번호(V)보다 작다 == 왼쪽 자식이 있다.
            if node_no * 2 + 1 <= V:
                tree[node_no][1] = int(input_data[3])


def inorder(node_no):
    if tree[node_no][2]:
        inorder(tree[node_no][0])
        ans.append(tree[node_no][2])
        inorder(tree[node_no][1])