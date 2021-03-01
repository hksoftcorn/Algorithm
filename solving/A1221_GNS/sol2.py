import sys
sys.stdin = open("input.txt")


def solution(N, alien_list):
    # Translate All
    def translator(number):
        # 외계어로 번역
        if type(number) == int:
            if number == 0:
                return 'ZRO'
            elif number == 1:
                return 'ONE'
            elif number == 2:
                return 'TWO'
            elif number == 3:
                return 'THR'
            elif number == 4:
                return 'FOR'
            elif number == 5:
                return 'FIV'
            elif number == 6:
                return 'SIX'
            elif number == 7:
                return 'SVN'
            elif number == 8:
                return 'EGT'
            elif number == 9:
                return 'NIN'
        # 사람말로 번역
        elif type(number) == str:
            if number == 'ZRO':
                return 0
            elif number == 'ONE':
                return 1
            elif number == 'TWO':
                return 2
            elif number == 'THR':
                return 3
            elif number == 'FOR':
                return 4
            elif number == 'FIV':
                return 5
            elif number == 'SIX':
                return 6
            elif number == 'SVN':
                return 7
            elif number == 'EGT':
                return 8
            elif number == 'NIN':
                return 9

    human_list = list(map(translator, alien_list))
    human_list.sort()

    sorted_alien_list = map(translator, human_list)
    return ' '.join(sorted_alien_list)


T = int(input())

for tc in range(1, T+1):
    N = int(input().split()[1])
    print("#{}\n{}".format(tc, solution(N, input().split())))



