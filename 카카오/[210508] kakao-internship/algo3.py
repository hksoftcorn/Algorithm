
def move_command(arr, c, k):
    direct, cnt = c.split()
    cnt = int(cnt)

    if direct == 'D':
        while cnt:
            k += 1
            cnt -= arr[0][k]

    else: # U일 경우
        while cnt:
            k -= 1
            cnt -= arr[0][k]

    return k


def delete_command(arr, stack, k):
    arr[0].pop(k)
    stack += [k]

    if k == len(arr[0]) - 2:
        k -= 1
    return k


def cancel_command(arr, stack, k):
    ele = stack.pop()
    arr[0].insert(ele, 1)
    if ele < k:
        k += 1
    return k



def solution(n, k, cmd):
    answer = ''
    arr = [[1] * n]
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
        if i in stack:
            answer += 'X'
        else:
            answer += 'O'

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))