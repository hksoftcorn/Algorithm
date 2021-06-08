import math
def solution(progresses, speeds):
    completed_days = []
    N = len(progresses)
    for idx in range(N):
        completed_days.append(int(math.ceil((100 - progresses[idx]) / speeds[idx])))

    cnt = 0
    bigger_num = -1
    result = []
    for i, day in enumerate(completed_days):
        if bigger_num <= day:
            bigger_num = day
            result += [cnt]
            cnt = 1
        else:
            cnt += 1

        if i == (N - 1):
            result += [cnt]

    return result[1:]


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))


##########
from math import ceil

days_left = list(map(lambda x, y: ceil((100 - x) / y), progresses, speeds))

def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
