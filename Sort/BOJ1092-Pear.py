# https://www.acmicpc.net/problem/1092

# import heapq, sys
#
#
# # del, extend
#
# def solution(l, p, s):
#     if max(l) < max(p):  # 실을수 없는 경우 빠꾸
#         print(-1)
#
#     p.sort(reverse=True)
#     # 해결 아이디어
#     # 가장 큰거 부터 넣어버리자~
#     # ㅇㅋ?
#     # 갯수 세는거
#     count = 0
#
#     # 물건이 있으면
#     while 1:
#         # print(p)
#         q = []  # 큐 사용
#
#         # 물건이 없으면 끝내고
#         if len(p) == 0:
#             break
#         # 큐에 크레인들을 넣어 준다 최대힙
#         for element in l:
#             heapq.heappush(q, -element)
#         # 시간초 하나 증가
#         count += 1
#
#         # 물건 번호
#         tempcount = 0
#         # 크레인 이 있으면
#         while 1:
#             # print(q)
#
#             # 크레인이 없으면 종료
#             if len(q) == 0:
#                 break
#             # 물건도 없을 경우 종료
#             if len(p) == 0:
#                 break
#
#             # if tempcount >= s:
#             #     print(-1)
#             #     return
#             # 만약 물건이 무게가, 크레인이 무게보다 작거나 같다면
#             if p[tempcount] <= -(q[0]):
#                 heapq.heappop(q)  # 크레인 빼버리고
#                 del p[tempcount]  # 물건에서 삭제한다.
#                 tempcount = 0  # 다시 물건 번호는 영번 부터
#                 continue  # 다음물건 적재하러
#             # 적재할수 없으면  증가해서 다음 거로 넘어간다
#             tempcount += 1
#             # 만약에 더이상 적재를 할 수가 없다면 이번턴은 끝내준다
#             if (-min(q)) < min(p):
#                 break
#
#     print(count)
#
#
# if __name__ == '__main__':
#     n = 3
#     l = [6, 8, 9]
#     s = 5
#     p = [2, 5, 2, 4, 7]
#     #
#     n = int(sys.stdin.readline())
#     l = list(map(int, sys.stdin.readline().split()))
#     s = int(sys.stdin.readline())
#     p = list(map(int, sys.stdin.readline().split()))
#
#     solution(l, p, s)


# # 시간초과 풀이
# import sys
# N = int(input())
# limits = map(int, sys.stdin.readline().split()) # 크레인 별 무게 제한
# M = int(input())
# packages = map(int, sys.stdin.readline().split()) # 화물 별 무게
#
# # 무게 제한과 화물 무게 전부 내림차순으로 정렬
# limits = sorted(limits, reverse=True) #므게
# packages = sorted(packages, reverse=True) #화불
#
# # 무게 제한이 제일 높은 크레인도 제일 무거운 화물을 들 수 없는 경우
# if packages[0] > limits[0] :
#     print(-1)
#     exit()
#
# answer = 0
# # 화물이 전부 옮겨질 때까지
# while len(packages) > 0:
#     answer += 1
#     # 무게제한을 돌면서 옮길 수 있는 화물을 옮김
#     for l in limits:
#         #화물으 돌면서
#         for j in range(len(packages)):
#             if l >= packages[j]: # 화물을 옮길 수 있으면
#                 del packages[j] # 화물 삭제  # 델 은 삭제
#                 break # 그다음 크레인으로 이동
# print(answer)



import sys

input = sys.stdin.readline
N = int(input())
crane_limit = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crane_limit.sort(reverse=True)
boxes.sort(reverse=True)
size, ans = 0, 0

if boxes[0] > crane_limit[0]:
    print(-1)
    sys.exit(0)
else:
    if M % N == 0:
        size = M // N
    else:
        size = M // N + 1

    while size > 0:
        ans += 1
        for i in range(N):
            for j in range(M):
                if boxes[j] <= crane_limit[i] and boxes[j] != 0:
                    boxes[j] = 0
                    break
        size -= 1

print(ans)