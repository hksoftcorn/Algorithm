def solution(n, lost, reserve):
    answer = n - len(lost)
    # 딕셔너리가 훨씬 빠르지 않을까? ㄴㄴ 비슷할 듯
    # reserves = {i : 1 for i in reserve}
    reserves = [0] * (n + 1)
    for r in reserve:
        if r in lost:
            lost.remove(r)
            answer += 1
            continue
        reserves[r] = 1
    
    for l in lost:
        if reserves[l-1]:
            reserves[l-1] -= 1
            answer += 1
        elif (l+1) <= n and reserves[l+1]:
            reserves[l+1] -= 1
            answer += 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))