# https://www.acmicpc.net/problem/11286
# 절대값힙

import heapq
import sys

input = sys.stdin.readline


# 튜플을 사용
# 원리 첫번째 원소로 heap 이 정렬 되기때문에 이렇게 되었다.
def solution(l):
    answer = []

    # 배열에서 꺼네서
    for element in l:
        # 0이 아니면
        if element != 0:
            # 절대값인 거로 넣고
            heapq.heappush(answer, (abs(element), element))
        else: # 0이면
            if answer: # 배열이 비어있지 않으면 값 출력
                print(heapq.heappop(answer)[1])
            else: # 배열이 비ㅓ있으면 0 출력
                print(0)


if __name__ == '__main__':
    s = 18
    l = [1,
         -1,
         0,
         0,
         0,
         1,
         1,
         -1,
         -1,
         2,
         -2,
         0,
         0,
         0,
         0,
         0,
         0,
         0]

    s = int(input())
    l = [int(input()) for _ in range(s)]

    (solution(l))
