N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def solution():
    cnt = len(A)
    arr = [a - B if a - B > 0 else 0 for a in A]
    for i in range(len(arr)):
        number = arr[i]
        if number:
            cnt += (number // C)
            if number % C:
                cnt += 1
    print(cnt)

solution()