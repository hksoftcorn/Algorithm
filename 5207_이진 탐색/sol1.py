import sys; sys.stdin = open('sample_input.txt', 'r')

def binary_search(arr, low, high, key):
    global cnt
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if key == arr[mid]:
            cnt += 1
            return mid
        elif key < arr[mid]:
            return binary_search(arr[:mid], low, mid - 1, key)
        else:
            return binary_search(arr[mid:], mid + 1, high, key)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        binary_search(B, 0, M-1, A[i])
    print(cnt)