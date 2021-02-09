import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):

    length = int(input())
    height = list(map(int, input().split()))

    result = 0

    for idx in range(2, length-2):
        l1, l2, current, r1, r2 = [height[idx+n] for n in range(-2,3)]

        sides = [l1, l2, r1, r2]