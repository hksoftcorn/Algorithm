def solution(priorities, location):
    cnt = 1
    while priorities:
        max_num = max(priorities)
        cur_n = priorities.pop(0)
        if max_num > cur_n:
            if location > 0:
                priorities.append(cur_n)
                location -= 1
            else:
                priorities.append(cur_n)
                location += (len(priorities) - 1)

        else: # max_num == cur_n
            if not location:
                return cnt
            else:
                cnt += 1
                location -= 1


priorities = [1, 1, 9, 1, 1, 1]
priorities = [2, 1, 3, 2]

location = 0
location = 2
print(solution(priorities, location))


