
numbers = list(range(1, 11))
is_selected = [None] * len(numbers)
result = []


def power_set(idx):
    # is_selected를 다 채우지 못 했다면
    if idx < len(numbers):
        is_selected[idx] = True
        power_set(idx + 1)
        is_selected[idx] = False
        power_set(idx + 1)

    # 다 채웠다면 (idx == len(numbers))
    else:
        total = 0
        for i in range(len(numbers)):
            if is_selected[i]:
                total += numbers[i]
        if total == 10:
            result.append(is_selected[:])
        return None

power_set(0)
print(result)