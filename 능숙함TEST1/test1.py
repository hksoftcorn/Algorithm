# string
def solution(string):
    max_cnt = 0
    for i in range(len(string)):
        s = string[i]
        tmp = string.count(s)
        if max_cnt < tmp:
            max_cnt = tmp
            max_str = s
    print(max_str, max_cnt)


string = 'asdasdada'
solution(string)
                