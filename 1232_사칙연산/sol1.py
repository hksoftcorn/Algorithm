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

        if len(input_data) == 4:
            tree[node_no][0] = int(input_data[2])
            tree[node_no][1] = int(input_data[3])
        elif len(input_data) == 3:
            tree[node_no][0] = int(input_data[2])


    def calc(a, b, x):
        if x == '+':
            return b + a
        elif x == '-':
            return b - a
        elif x == '*':
            return b * a
        elif x == '/':
            return b / a


    stack = []
    def solution(node_no):
        # 후위연산자로 풀어야하나??
        if tree[node_no][2]:
            solution(tree[node_no][0])
            solution(tree[node_no][1])

            if tree[node_no][2].isnumeric():
                stack.append(tree[node_no][2])
            else:
                a = stack.pop()
                b = stack.pop()
                tmp = calc(float(a), float(b), tree[node_no][2])
                stack.append(tmp)


    solution(1)
    print('#{} {}'.format(tc, int(*stack)))

