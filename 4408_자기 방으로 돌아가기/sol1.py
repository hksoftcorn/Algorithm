import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    current_room, my_room = map(int, input().split())
    steps = [i for i in range(current_room, my_room+1)]
    result = 1

    for _ in range(N-1):
        current_room, my_room = map(int, input().split())
        for i in range(current_room, my_room+1):
            if i in steps:
                result += 1
                break
        steps = [i for i in range(current_room, my_room+1)]
    print('#{} {}'.format(tc, result))

## 아 모든 학생이 동시에 출발??!
