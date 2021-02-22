# import sys
# sys.stdin = open('1번_input.txt', 'r')


def solution(N, M, arr):
    """ N x M 크기의 정원에서 나무를 심은 총 비용, 심은 나무의 총 수, 가장 비싼 나무의 가격, 비싼 나무의 열위치를 반환합니다.

    Parameter
        N  (int) : 행의 개수
        M (int) : 열의 개수
        arr (array) : 입력받은 2차원 배열

    return
        total_cost : 나무를 심은 총 비용
        total_count : 심은 나무의 총 수
        max_cost : 가장 비싼 나무의 가격
        max_cost_col : 비싼 나무의 열위치
    """

    N = N
    M = M
    arr = arr

    # 1. 심은 나무의 총 수 = (열의 홀수 개수) * 행의 개수
    total_count = ((M+1)//2) * N
    total_cost = 0
    max_cost = 0
    max_cost_col = 0

    # 2. 열 우선순회 : 홀수 열(j) 순회, 모든 행(i) 순회
    for j in range(0, M, 2):
        cost = 0
        for i in range(N):
            # 2.1. 열의 모든 원소들의 합을 cost 변수에 더함
            cost += arr[i][j]
            # 2.2. max_cost와 max_cost_row를 찾음
            if max_cost <= arr[i][j]:
                max_cost = arr[i][j]
                max_cost_col = j + 1
        # 2.3. cost를 더하여 total_cost를 구함
        total_cost += cost

    # 3. 나무를 심은 총 비용, 심은 나무의 총 수, 가장 비싼 나무의 가격, 비싼 나무의 열위치를 반환
    return total_cost, total_count, max_cost, max_cost_col


# 테스트 케이스를 입력받습니다
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, ' '.join(map(str, solution(N, M, arr)))))