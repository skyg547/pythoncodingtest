# # 컵라면
# # 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# # 2 초	256 MB	4276	1274	917	30.803%
# # 문제
# # 상욱 조교는 동호에게 N개의 문제를 주고서, 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시 하였다. 하지만 동호의 찌를듯한 자신감에 소심한 상욱 조교는 각각의 문제에 대해 데드라인을 정하였다.
# #
# # 문제 번호	1	2	3	4	5	6	7
# # 데드라인	1	1	3	3	2	2	6
# # 컵라면 수	6	7	2	1	4	5	1
# # 위와 같은 상황에서 동호가 2, 6, 3, 1, 7, 5, 4 순으로 숙제를 한다면 2, 6, 3, 7번 문제를 시간 내에 풀어 총 15개의 컵라면을 받을 수 있다.
# #
# # 문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것이다. 위의 예에서는 15가 최대이다.
# #
# # 문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수이다. 또, 각 문제를 풀 때 받을 수 있는 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 231보다 작거나 같은 자연수이다.
# #
# # 입력
# # 첫 줄에 숙제의 개수 N (1 ≤ N ≤ 200,000)이 들어온다. 다음 줄부터 N+1번째 줄까지 i+1번째 줄에 i번째 문제에 대한 데드라인과 풀면 받을 수 있는 컵라면 수가 공백으로 구분되어 입력된다.
# #
# # 출력
# # 첫 줄에 동호가 받을 수 있는 최대 컵라면 수를 출력한다.
#
#
# #
# # 4% 시간초과
# # pypy 오답
# def solution(l):
#     # 정렬
#     l.sort(key=lambda x: x[0])
#     # print(l)
#     ans = 0
#
#     maxtime = max(l[0])
#
#     for time in range(200000):
#         # 시간초 넘치면 제거
#         if l[-1][0] < time:
#             break
#         secondtime = time + 1
#         temp = [0]  # 값들을 담아줄 그릇
#
#         # 컵라면을 돌면서
#         for problem in l:
#             # 시간초 안에 있는 것들을 담기
#             if problem[0] == secondtime:
#                 temp.append(problem[1])
#             if not temp:
#                 secondtime += 1
#
#         ans += max(temp)
#
#     return ans
#
#
# if __name__ == '__main__':
#     n = 7
#     l = [[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]]
#
#     n = int(input())
#     l = [list(map(int, input().split())) for _ in range(n)]
#
#     print(solution(l))

import sys
import _heapq
from collections import deque

# 인풋 바꿔주가
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# 정렬
arr = sorted(arr, key=lambda k: k[0])

# 큐에 넣기
arr = deque(arr)
# 힙
heap = []
# 연산결과
res = 0
# 거꾸로 진행 -1 씩
# 최대힙으로 끄내기
for time in range(n, 0, -1):
    # 배열이 있고 , 배열 마지막 값 시간이 시간다 크거나 같다면
    while arr and arr[-1][0] >= time:
        # 힙 푸시
        _heapq.heappush(heap, -arr.pop()[1])
    # print(heap)
    # 힙 이 있으면 최대값 끄내기
    if heap:
        res -= _heapq.heappop(heap)
print(res)
