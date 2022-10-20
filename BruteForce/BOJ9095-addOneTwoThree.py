# https://www.acmicpc.net/problem/9095
# 1,2,3 더하기

import sys

shortCutInput = sys.stdin.readline


# f(1)
# 1

# f(2)
# 1 +1
# 2

# f(3)
# 1+1+1
# 2+ 1
# 1+2
# 3

# f(4)
#  f(1) + f(2) + f(3)  1, 2, 3 이니 각 이전 갯수에 1 ,2, 3 을 더 해주면 뇐다


def getNumberList():
    tneoNumberList = [0] * 10
    tneoNumberList[0] = 1
    tneoNumberList[1] = 2
    tneoNumberList[2] = 4

    for index in range(3, len(tneoNumberList)):
        tneoNumberList[index] = tneoNumberList[index - 1] + tneoNumberList[index - 2] + tneoNumberList[index - 3]

    return tneoNumberList


if __name__ == '__main__':
    numberList = getNumberList()

    iterableCount = int(shortCutInput())

    for _ in range(iterableCount):
        print(numberList[int(shortCutInput()) - 1])
