# # 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# # 1 초	256 MB	16869	3864	2701	22.306%
# # 문제
# # 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
# #
# # 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
# #
# # 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
# #
# # 입력
# # 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
# #
# # 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
# #
# # 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
# #
# # 모든 숫자는 양의 정수이다.
# #
# # 출력
# # 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

# def solution(l, b):
#     maxb = max(b)
#     # 가치에 맞게 정렬 --여기서 시간초과
#     l.sort(key=lambda x: x[1], reverse=True)
#     # 최대값을 구할 변수
#     anssum = 0
#
#     # 가치 높은 보석을 돌면서
#     for i in l:
#         # 보석 무게가 가방 최대 보다 무거우면 못담고
#         if i[0] > maxb:
#             break
#         # 보석 무게와 가방의 차이를 구할 최소값
#         min = 1e9
#         minindex = 0
#
#         # 가방의 비어있지 않을때
#         if b:
#             # 가방을 돌아가며
#             for j in b:
#                 # 보석무게와 가장 차이가 적은 걸 구해주며
#                 # print(b,j)
#                 if abs(i[0] - j) < min:
#                     min = abs(i[0] - j)
#                     minindex = j
#                     # print(minindex)
#
#             # 담은 가방은 제거
#             b.remove(minindex)
#             # print(b,'removed')
#             # 보석 가치 더하기
#             anssum += i[1]
#
#     # print(l)
#     return anssum
#
#
#
#
#
# if __name__ == '__main__':
#     n, k = 3, 2
#     lists = [[1, 65],
#              [5, 23],
#              [2, 99]
#              ]
#     bag = [10, 2]
#
#     n, k = map(int, input().split())
#
#     lists = []
#     for _ in range(n):
#         x1, x2 = map(int, input().split())
#         lists.append([x1, x2])
#     # lists = list(map(lambda x1, x2: list(int(x1), int(x2)), input().split()) for _ in range(n))
#
#     # lists = []
#     # bag = []
#     # for _ in range(k):
#     #     bag.append(map(int, input()))
#     bag = [int(input()) for _ in range(k)]
#
#     # print(lists)
#     # print(bag)
#     print(solution(lists, bag))


#인터넷 해설
import sys
import heapq

N,K = map(int, sys.stdin.readline().split())
jew = []

# 힙으로 정렬 하면서 입력
for _ in range(N):
    heapq.heappush(jew, list(map(int,sys.stdin.readline().split())))
print(jew)

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()

answer =0
tmp_jew = []

#작은 가방부터 돌면서
for bag in bags:
    # 보석이 있고, 가방 무게가 더 크면
    while jew and bag >= jew[0][0]:
        #임시 보석에 보석 가치 추가, 보석 제거
        heapq.heappush(tmp_jew,-heapq.heappop(jew)[1])
    if tmp_jew:
        #정답에 임시  보석가치를 더해주고 제거
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)