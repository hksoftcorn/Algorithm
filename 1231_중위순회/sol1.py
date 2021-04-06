T = 10

for tc in range(1, T+1):
    N = int(input())
    # 2차원 배열
    # arr = [[0] * (N + 1) for _ in range(3)]

    word = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        input_data = list(input().split())
        V = int(input_data[0])
        word[V] = input_data[1]

        if len(input_data) == 4:
            left[V] = int(input_data[2])
            right[V] = int(input_data[3])
        elif len(input_data) == 3:
            left[V] = int(input_data[2])

    def inorder(n):
        if n == 0:
            return
        else:
            inorder(left[n])
            print(word[n], end='')
            inorder(right[n])

    print('#{} '.format(tc), end='')
    inorder(1)
    print()

# INCORRECT1. 왜 자꾸 None이 붙지???
# print(inorder(1)) -> None....

# INCORRECT2. print
# 테스트케이스 붙이기 및 print() 넣어주기