
def move_command(arr, c, k):
    direct, cnt = c.split()
    cnt = int(cnt)

    if direct == 'D':
        while cnt:
            k += 1
            cnt -= arr[k]

    else: # U일 경우
        while cnt:
            k -= 1
            cnt -= arr[k]

    return k


def delete_command(arr, stack, k):
    arr[k] = 0
    stack += [k]
    k += 1

    if k >= len(arr):
        k -= 1
        while arr[k] == 0:
            k -= 1
    else:
        while arr[k] == 0:
            k += 1
    return k


def cancel_command(arr, stack, k):
    ele = stack.pop()
    arr[ele] = 1
    return k


def solution(n, k, cmd):
    answer = ''
    arr = [1] * n
    stack = []

    for c in cmd:
        # D 혹은 U
        if len(c) > 1:
            k = move_command(arr, c, k)
            # print(k)
        else:
            if c == 'C':
                k = delete_command(arr, stack, k)
                # print('C', arr, stack, k)
            else:
                k = cancel_command(arr, stack, k)
                # print('Z', arr, stack, k)


    for i in range(n):
        if arr[i]:
            answer += '0'
        else:
            answer += 'X'

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))