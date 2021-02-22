# import sys
# sys.stdin = open('2번_input.txt', 'r')


def solution(start, A_number, B_number):
    """마지막 칸에 먼저 도달한 사람을 반환합니다. 아무도 도착하지 못하면 무승부로 게임이 종료됩니다.

    :parameter
         start :  처음 시작 선수
         A_number : A의 이동 값
         B_number : B의 이동 값

     :return
        A or B : 20번째 칸에 먼저 도달한 사람을 반환합니다.
        AB : 아무도 도착하지 못하면 무승부로 게임이 종료됩니다.
    """
    start = start
    A_number = A_number
    B_number = B_number

    # 1. 게임 규칙을 적용한 함수를 구현합니다
    def playing_game(first, second):
        # 1.1. 첫 번째 플레이어와 두 번째 플레이어 위치를 초기화 합니다.
        first_player_position = 0
        second_player_position = 0

        # 2. 10번의 말 이동 기회가 있습니다.
        for idx in range(10):
            # 2.1. 첫 번째 선수가 말을 옮깁니다.
            first_player_position += first[idx]
            # 2.2. 만약 두 번째 선수의 말과 같은 위치로 옮겨졌다면, 두 번째 선수의 말은 처음 위치로 갑니다.
            if first_player_position == second_player_position:
                second_player_position = 0
            # 2.3. 첫 번째 선수의 말 위치가 19(20번째) 이상이 되면 게임이 종료됩니다.
            if first_player_position >= 19:
                # 2.4. return 값으로 f를 반환합니다.
                return 'f'

            # 3.1. 마찬가지로 두 번째 선수가 말을 옮깁니다.
            second_player_position += second[idx]
            if second_player_position == first_player_position:
                first_player_position = 0
            if second_player_position >= 19:
                # 3.2. return 값으로 s를 반환합니다.
                return 's'
        # 4. 만약 10번 이내에 게임이 끝나지 않는다면, return 값으로 None을 반환합니다.
        return None

    # 5. 첫 스타트 선수를 분류합니다. A 선수 시작.
    if start == 'A':
        # 5.1. 위에서 정의한 게임함수를 이용하여 result 값을 반환합니다.
        result = playing_game(A_number, B_number)
        if result == 'f':
            return 'A'
        elif result == 's':
            return 'B'
        else:
            return 'AB'

    else:
        # 5.2. 마찬가지로 B 선수가 처음으로 시작했을 때 result 값을 반환합니다.
        result = playing_game(B_number, A_number)
        if result == 'f':
            return 'B'
        elif result == 's':
            return 'A'
        else:
            return 'AB'


# 테스트 케이스를 입력받습니다
T = int(input())

for tc in range(1, T+1):
    start = input()
    A_number = list(map(int, input().split()))
    B_number = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution(start, A_number, B_number)))

