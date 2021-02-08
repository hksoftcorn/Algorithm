import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, list(input())))


for idx in range(len(counter)):
    if counter[idx] >= 3:
        is_babygin += 1
        counter[idx] -= 3

    if idx < 8:
        if counter[idx] != 0 and counter[idx+1] != 0 and counter[idx+2] != 0:
            is_babygin += 1
            counter[idx] -= 1
            counter[idx+1] -= 1
            counter[idx+2] -= 1

