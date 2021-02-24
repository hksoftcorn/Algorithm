import sys
sys.stdin = open('input.txt', 'r')


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    # pivot 기준으로 작은 숫자들은 left, 큰 숫자들은 right에 모은다.
    left, right = [], []
    pivot = numbers[0]

    for num in numbers:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    quick_sort(left)
    quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    print('#{} {}'.format(tc, quick_sort(numbers)))