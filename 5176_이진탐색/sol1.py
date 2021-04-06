T = int(input())

for tc in range(1, T+1):
    V = int(input())
    # 루트노드
    root_node = V // 2 + 1


    print('#{} {} {}'.format(tc, root_node, ans))




# 오답 케이스
# T = int(input())
#
# for tc in range(1, T+1):
#     V = int(input())
#     root_node = V // 2 + 1
#     # 마지막 노드(V)의 부모노드 : remainder_parent_node
#     # 마지막 노드의 숫자는 홀수로 증가합니다.
#     cnt = 0
#     tmp = V
#     while tmp != 1:
#         tmp //= 2
#         cnt += 1
#
#     remainder_idx = V - (2 ** (cnt))
#     remainder = 2 * remainder_idx + 1
#     if remainder_idx % 2:
#         remainder_parent_node = remainder - 1
#     else:
#         remainder_parent_node = remainder + 1
#
#     print('#{} {} {}'.format(tc, root_node, remainder_parent_node))