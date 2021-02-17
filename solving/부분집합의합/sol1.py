numbers = [1, 2, 3, 4]
input()
for i in range(1, 1 << len(numbers)):
    total = 0
    for j in range(len(numbers)):
        if i & (1 << j):
            print(numbers[j], end=' ')
            total += numbers[j]
    print()
