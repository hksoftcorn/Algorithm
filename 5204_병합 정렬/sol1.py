import sys; sys.stdin = open('sample_input.txt', 'r')

def merge_sort(numbers):
    global cnt

    N = len(numbers)
    # base case
    if N < 2:
        return numbers
    
    mid_idx = N // 2
    left = numbers[:mid_idx]
    right = numbers[mid_idx:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        if sorted_left[l] <= sorted_right[r]:
            merged.append(sorted_left[l])
            l += 1
        else:
            merged.append(sorted_right[r])
            r += 1

    if l < len(sorted_left):
        cnt += 1

    while l < len(sorted_left):
        merged.append(sorted_left[l])
        l += 1
    while r < len(sorted_right):
        merged.append(sorted_right[r])
        r += 1

    return merged      


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    input_data = list(map(int, input().split()))
    cnt = 0 
    result = merge_sort(input_data)
    
    print('#{} {} {}'.format(tc, result[N//2], cnt))
