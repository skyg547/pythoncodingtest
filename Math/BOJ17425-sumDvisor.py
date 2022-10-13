# https://www.acmicpc.net/problem/17425# 약수의 합
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

inputShortCut = sys.stdin.readline

def getSumDivisorList(maxNumber):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sumDivisorList = [0] * maxNumber

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(1, maxNumber):
        for j in range(1, maxNumber):  # i이후 i의 1배수들을 False 판정
            sumDivisorList[i*j] += i
        sumDivisorList[i] += sumDivisorList[i-1]

    # 소수 목록 산출
    return sumDivisorList

if __name__ == '__main__':
    # iterationsNumber = int(inputShortCut())
    # maxNumbers = [int(inputShortCut()) for _ in range(iterationsNumber)]

    maxNumbers = 100000001
    maxNumber = 10000001
    sumDivisorList = [0] * maxNumbers

    # for maxNumber in range(1, maxNumbers):
    sumDvisors = 0
    for number in range(1, maxNumber + 1):
        sumDvisors += (maxNumber // number) * number
        # sumDivisorList[maxNumber] = sumDvisors

    print(sumDvisors)

# for maxNumber in maxNumbers:
#     sumDvisors = 0
#     for number in range(1, maxNumber + 1):
#         sumDvisors += (maxNumber // number) * number
#     print(sumDvisors)
