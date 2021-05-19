def solution(tickets):
    answer = []
    trips = {}
    for ticket in tickets:
        departure, destination = ticket
        trips[departure] = trips.get(departure, []) + [destination]
    
    trips = {key : sorted(trips[key]) for key in trips.keys()}

    # def travel(v):
    #     cur_v = v
    #     while trips.get(cur_v, 0):
    #         next_v = trips[cur_v].pop(0)
    #         answer.append(next_v)
    #         cur_v = next_v

    # def dfs(v):
    #     Q = [v]
    #     if trips.get(v, 0):
    #         next_v = trips[v].pop(0)
    #         answer.append(next_v)
    #         dfs(next_v)

    def dfs(v):
        while trips.get(v, 0):
            dfs(trips[v].pop(0))
        answer.append(v)
    
    # print(trips)
    dfs("ICN")
    return answer[::-1]

sample2= [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(sample2))