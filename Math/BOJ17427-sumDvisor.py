# https://www.acmicpc.net/problem/17427
# 약수의 합
# 10 까지의 모든 약수의 합을 더한것

# N = 10일때를보자.
#
# f(1) = sum(1)
# f(2) = sum(1, 2)
# f(3) = sum(1, 3)
# f(4) = sum(1, 2, 4)
# f(5) = sum(1, 5)
# f(6) = sum(1, 2, 3, 6)
# f(7) = sum(1, 7)
# f(8) = sum(1, 2, 4, 8)
# f(9) = sum(1, 3, 9)
# f(10) = sum(1, 2, 5, 10)
#
# 이고 각각 10까지에 약수 숫자들의 갯수를 카운팅해보면,
#
# 1: 10개(10을1로나눈몫)
# 2: 5개(10을2로나눈몫)
# 3: 3개(10을3으로나눈몫)


import sys
import math
from collections import deque

inputShortCut = sys.stdin.readline

if __name__ == '__main__':
    maxNumber = int(inputShortCut())
    dvisors = deque()
    for number in range(1, maxNumber + 1):
        for dvisor in range(1, number + 1):
            # print(dvisor)
            # print(number % dvisor)
            if number % dvisor == 0:
                dvisors.append(dvisor)

    print(sum(dvisors))
