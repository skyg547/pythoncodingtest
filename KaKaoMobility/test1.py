from collections import deque
from itertools import permutations
from itertools import combinations
import sys

input = sys.stdin.readline

def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0:
            print(0)
        else :
            print(N % 10, end="")
        N = N // 10

if __name__ == '__main__':
    solution(int(input()))