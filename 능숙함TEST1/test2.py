"""
연속된 N개 구간에서,
어떤 알파벳이 가장 많이 등장할까?
"""
def solution(string, N):
    my_dict = {}
    L = len(string)

    for i in range(L - N + 1):
        new_string = string[i : i + N]
        new_set = set(new_string)
        for s in new_set:
            tmp = new_string.count(s)
            my_dict[s] = my_dict.get(s, 0) + tmp
    
    max_cnt = 0
    print(my_dict)
    
    for k, v in my_dict.items():
        if max_cnt < v:
            max_cnt = v
            max_str = k
    print(max_str, max_cnt)

string = 'SSADADAAASADAAAS'
N = 5
solution(string, N)