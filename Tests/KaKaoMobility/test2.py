from collections import deque
from itertools import permutations
from itertools import combinations
# 무방향 그래프
#  m 인 두개의 배열 a, b
# k 가 0에서 m-1 까지 kdp eo
import sys

input = sys.stdin.readline


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    # write your code in Python 3.8.10
    links = list(sorted(map(lambda x: sorted(x), zip(A, B)))) # 간선
    isRightPath = True # 올바른 경로 구분
    for node in range(1, N): # 목표 지점까지 반복
        if [node, node + 1] in links: # 간선 있을 시
            continue
        else:
            isRightPath = False # 간선 없을 시
            break
    print(isRightPath)


if __name__ == '__main__':
    solution(6, [2,4,5,3], [3,4,6,4])
