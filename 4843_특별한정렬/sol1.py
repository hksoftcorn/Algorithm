import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    bubble_sort(numbers)

    result = []
    for i in range(5):
        result.append(numbers[-(i+1)])
        result.append(numbers[i])

    print('#{} {}'.format(tc, " ".join(str(i) for i in result)))
