import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(1, T+1):
    tc, l = input().split()
    my_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    my_dict = {l:0 for l in my_list}

    input_data = list(input().split())
    for data in input_data:
        my_dict[data] += 1

    result = []
    print(tc)
    for key in my_list:
        for _ in range(my_dict[key]):
            print(key, end=' ')
    print()








