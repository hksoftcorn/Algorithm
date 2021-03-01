numbers = [1, 2, 3, 4]
for i in range(1, 1 << len(numbers)):
    total = 0
    parts = []
    for j in range(len(numbers)):
        if i & (1 << j):
            parts.append(numbers[j])
    print(parts)
