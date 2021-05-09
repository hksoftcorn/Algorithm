dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]
def isDistance(arr):
    for r in range(5):
        for c in range(5):
            if arr[r][c] == 'P':
                # 1. 상하좌우 검색
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if arr[nr][nc] == 'X': continue
                        if arr[nr][nc] == 'P':
                            return 0
                        nr += dr[i]
                        nc += dc[i]
                        if 0 <= nr < 5 and 0 <= nc < 5:
                            if arr[nr][nc] == 'X': continue
                            if arr[nr][nc] == 'P':
                                return 0

                # 2. 대각선 검색
                for j in range(4):
                    nx = r + dx[j]
                    ny = c + dy[j]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if arr[nx][ny] == 'P':
                            if arr[nx][c] != 'X' or arr[r][ny] != 'X':
                                return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        result = isDistance(place)
        answer += [result]

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))