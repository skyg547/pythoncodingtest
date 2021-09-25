# # 터렛
# # https://www.acmicpc.net/problem/1002
# import math
#
#
# def solution(alllists):
#     for lists in alllists:
#         distance = lists[2] + lists[-1]
#
#         distanceFor2People = int(math.sqrt((lists[0] - lists[3]) ** 2 + (lists[1] - lists[4]) ** 2))
#
#         # 같지 않은 경우
#         if distanceFor2People != 0:
#             # 거리가 더 클 때
#             if lists[-1] == distanceFor2People + lists[2] or lists[2] == distanceFor2People + lists[-1]:
#              print(1)
#             elif distance > distanceFor2People:
#                 # 2개 점 교차
#                 if not (distanceFor2People < lists[2] or distanceFor2People < lists[-1]):
#                     print(2)
#                 # 안쪽으로 포함
#                 else:
#                     print(0)
#                     # 외접
#             elif distance == distanceFor2People:
#                 print(1)
#                 # 내접
#             else:
#                 print(0)
#             # print(distance , distanceFor2People)
#         else:
#             if lists[2] == lists[-1]:
#                 print(-1)
#             else:
#                 print(0)
#     # 두 점과 거리와 길이가 같냐
#
#     # 두 점 거리와 길이가 작냐
#
#     # 두 점 거리와 길이가 크냐
#
#     return
#
#
# if __name__ == '__main__':
#     s = int(input())
#
#     lists = [list(map(int, input().split())) for _ in range(s)]
#
#     solution(lists)
#
#     # print(lists)


n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2) + +2 + (y1 - y2) ** 2) ** (1 / 2)
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)
    print(-1 if (r == 0 and r1 == r2) else 1 if (r == r1 + r2 or m == sum(R)) else 2)
