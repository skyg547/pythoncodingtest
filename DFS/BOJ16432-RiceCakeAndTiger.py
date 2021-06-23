# import sys
#
# input = sys.stdin.readline
# n = int(input())
# answer = [0] * n
# ricecake = []
# for _ in range(n):
#     ricecake.append(list(map(int, input().split()))[1:])
#
#
#
# def dfs(depth, last):
#     if depth == n:
#         return True
#     for num in ricecake[depth]:
#         if last != num:
#             answer[depth] = num
#             if dfs(depth + 1, num):
#                 return True
#     return False
#
#
# for i in range(n - 1):
#     # 절대 안되는 경우
#     if len(ricecake[i]) == 1 and len(ricecake[i + 1]) == 1 and ricecake[i][0] == ricecake[i + 1][0]:
#         print(-1)
#         exit(0)
#
# if dfs(0, 0):
#     for x in answer:
#         print(x)
# else:
#     print(-1)
#
#
