import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    one_day, one_month, three_month, one_year = map(int, input().split())
    swimming = list(map(int, input().split()))
    
