# https://www.acmicpc.net/problem/15596
# 정수 N개의 합

import sys


def solve(a):
    # https://www.acmicpc.net/problem/15596
    # 정수 N개의 합
    # 재귀 횟수 증가
    sys.setrecursionlimit(1000000)

    return sum(a)
