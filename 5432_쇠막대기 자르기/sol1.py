import sys
sys.stdin = open('sample_input.txt')


def solution(input_data):
    layer_iron_data = input_data
    iron_data = layer_iron_data.replace('()', '*')

    result = 0
    for idx in range(len(iron_data) -1):
        if iron_data[idx] == '(':
            pair = 1
            for pair_idx in range(idx+1, len(iron_data)):
                if iron_data[pair_idx] == '(':
                    pair += 1
                elif iron_data[pair_idx] == ')':
                    pair -= 1

                if pair == 0:
                    # count 메서드 구현
                    result += iron_data[idx:pair_idx+1].count('*') + 1
                    break
        else:
            continue

    return result


T = int(input())

for tc in range(1, T+1):
    input_data = input()
    print('#{} {}'.format(tc, solution(input_data)))