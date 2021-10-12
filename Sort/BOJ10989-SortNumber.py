# https://www.acmicpc.net/problem/10989
# 수정렬하기 3

import sys

input = sys.stdin.readline


def solution():
    return


if __name__ == '__main__':
    numberList = [0] * 10001

    N = int(input())

    for _ in range(N):
        numberList[int(input())] += 1

    for number, element in enumerate(numberList):
        for _ in range(element):
            print(number)
