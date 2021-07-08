# https://www.acmicpc.net/problem/14681
# 사분면 고르기

import sys


def solution(x, y):
    mul = x * y
    add = x + y

    if mul < 0 and add <= 0:
        if x < 0:
            return 2
        else:
            return 4

    elif mul < 0 <= add:
        if x > 0:
            return 4
        else:
            return 2
    elif mul > 0 > add:
        return 3

    else:
        return 1


if __name__ == '__main__':
    x = int(input())
    y = int(input())

    print(solution(x, y))
