# https://www.acmicpc.net/problem/3020
# 개똥벌레

import sys


def solution(h, l):
    # h 배열을 만들어 주자

    ar = [[0] * len(l) for _ in range(h)]
    # print(ar)
    # n * h 배열 만들기

    for i in range(len(l)):
        if i % 2 == 0:
            for j in range(l[i]):
                ar[j][i] = 1

        elif i % 2 == 1:
            for j in range(h - 1, h - 1 - l[i], -1):
                ar[j][i] = 1

    ar2 = []
    for i in ar:
        ar2.append(sum(i))
    # print(ar)
    #
    # print(ar2)
    minnnum = min(ar2)
    return minnnum, ar2.count(minnnum)

    # 넣어주고

    # 탐색

    # 탐색하자


if __name__ == '__main__':
    n, h = 14, 5
    l = [1, 3, 4, 2, 2, 4, 3, 4, 3, 3, 3, 2, 3, 3]

    n, h = map(int, sys.stdin.readline().split())
    l = [int(input()) for _ in range( n)]
    print(*solution(h, l))
