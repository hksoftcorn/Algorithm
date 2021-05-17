def solution(number, k):
    answer = ''
    number_list = list(number)
    N = len(number_list)
    n = N - k

    max_num = 0
    for i in range(N):
        if max_num < int(number_list[i]):
            max_num = int(number_list[i])

    def perm(k):
        if k == n:
            print(number_list)

        if int(number_list[0]) < max_num:
            # print(number_list)
            # return
            pass

        for i in range(k, N):
            number_list[i], number_list[k] = number_list[k], number_list[i]
            perm(k+1)
            number_list[i], number_list[k] = number_list[k], number_list[i]

    perm(0)

solution("1924", 2) # 94
print(1)