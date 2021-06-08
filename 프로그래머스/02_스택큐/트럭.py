def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    total_time = 0

    while queue:
        queue.pop(0)
        total_time += 1

        if truck_weights:
            if truck_weights and sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return total_time


bridge_length = 2
bridge_length = 100
weight = 10
weight = 100
truck_weights = [7,4,5,6]
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))




# SOL1
# def solution(bridge_length, weight, truck_weights):
#     queue = [0] * bridge_length
#     total_time = 0
#
#     while truck_weights:
#         if sum(queue) + truck_weights[0] <= weight:
#             cur_truck = truck_weights.pop(0)
#             queue.pop(0)
#             queue.append(cur_truck)
#             total_time += 1
#
#         else:
#             queue.pop(0)
#             queue.append(0)
#             if not sum(queue):
#                 cur_truck = truck_weights.pop(0)
#                 queue.pop(0)
#                 queue.append(cur_truck)
#             total_time += 1
#     else:
#         total_time += bridge_length
#
#     return total_time

