max_num = 0
def solution(numbers):
    n = len(numbers)
    numbers.sort(key=lambda x: str(x)[0], reverse=True)
    cur_num = int(''.join(map(str, numbers)))

    def perm(k, arr, cur_num):
        global max_num
        if int(str(cur_num)[0]) > arr[0]:
            return

        if k == n:
            tmp = int(''.join(map(str, arr)))
            if tmp > max_num:
                max_num = tmp

        else:
            for i in range(k, n):
                arr[k], arr[i] = arr[i], arr[k]
                perm(k+1, arr, cur_num)
                arr[k], arr[i] = arr[i], arr[k]

    perm(0, numbers, cur_num)
    return str(max_num)


# print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))