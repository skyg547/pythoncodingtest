# https://www.acmicpc.net/problem/17425# 약수의 합
# 10 까지의 모든 약수의 합을 더한것

# N = 10일때를보자.
# 약수는 = 배수가 되는 수

import sys

inputShortCut = sys.stdin.readline


def getSumDivisorList(maxNumber):
    # 에라토스테네스의 체 초기화:
    sumDivisorList = [1] * maxNumber

    # 모든 수를 돌면서
    for i in range(2, maxNumber):
        for j in range(1, maxNumber):  # 배수가 되는 수에 자신을 더함
            if i * j >= maxNumber:
                break
            sumDivisorList[i * j] += i
        sumDivisorList[i] += sumDivisorList[i - 1]  # 이게 없으면 약수의합  아니게 됨 , 있을 시 약수의 누적합

    # 소수 목록 산출
    return sumDivisorList


if __name__ == '__main__':
    iterationsNumber = int(inputShortCut())

    maxNumber = 1000001
    maxNumbers = getSumDivisorList(maxNumber)

    for number in range(iterationsNumber):
        print(maxNumbers[int(inputShortCut())])
