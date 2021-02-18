import sys
sys.stdin = open('GNS_test_input.txt')


def solution(N, alien_list):

    def translator(number):
        if type(number) == int:

        elif type(number) == str:

    print()

T = int(input())

for tc in range(1, T + 1):
    N = int(input().split()[1])

    print('#{}\n{}'.format(tc, solution(tc, input().split())))