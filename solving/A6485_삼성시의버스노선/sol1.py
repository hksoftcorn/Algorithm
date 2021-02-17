import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    all_stations = [0 for _ in range(5000)]
    N = int(input())  # 버스 노선 개수
    for _ in range(N):
        start, end = map(int, input().split())
        # 버스 노선 시작부터 끝까지(index 기준으로는 -1)
        for station in range(start-1, end):
            all_stations[station] += 1

    P = int(input())  # 체크할 정류장 번호 개수
    result = []
    for _ in range(P):
        check = int(input())  # check 할 정류장 번호
        result.append(all_stations[check-1])  # index 기 때문에 -1

    print('#{} {}'.format(tc, " ".join(map(str, result))))
