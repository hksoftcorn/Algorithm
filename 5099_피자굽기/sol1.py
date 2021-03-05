import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    pizzas_idx = [(pizzas[i], i+1) for i in range(len(pizzas))]
    queue = [pizzas_idx.pop(0) for _ in range(N)]

    while len(queue) != 1:
        pizza = queue.pop(0)
        half_pizza = pizza[0] // 2

        if half_pizza:
            queue.append((half_pizza, pizza[1]))
        else:
            if pizzas_idx:
                new_pizza = pizzas_idx.pop(0)
                queue.append(new_pizza)

    print('#{} {}'.format(tc, queue[0][1]))