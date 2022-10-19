# https://www.acmicpc.net/problem/9095
# 1,2,3 더하기

import sys

shortCutInput = sys.stdin.readline
if __name__ == '__main__':
    n = int(shortCutInput())

    numberList = [0]*10
    numberList[0] = 1
    numberList[1] = 2
    numberList[2] = 3

    for i in range (3, len(numberList)):
        numberList[i] = numberList[i-1]*2 +1

    print(numberList)

    #
    # 1 1 *2 +1
    #
    # 1+1 2
    # 2
    #
    # 1+1+1 3 *2 +1
    # 1+2 2
    # 2+1
    # 3
    #
    # 1+1+1+1    7
    # 1+1+2
    # 1+2+1
    # 2+1+1
    # 2+2
    # 3+1 3
    # 1+3 3
    #
    # 1+4 14
    # 4+1 14 +1
    #자기 자신 +1
    # 1, 1+1, 1+1+1, :
