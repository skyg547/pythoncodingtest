# https://www.acmicpc.net/problem/1929
# 1
# 소수 구하기
#

from audioop import add
import sys
import math
from collections import deque

shortcutInput = sys.stdin.readline


def isPrimeNumber(testNumber):
    for number in range(2, testNumber):
        if testNumber % number == 0:
            return False
    return True


startNumber, endNumber = map(int, shortcutInput().split())

numberLIst = deque(range(startNumber, endNumber))
primeList = set()
notPrimeList = set()

while len(numberLIst) != 0:

    testNumber = numberLIst.popleft()
    if testNumber in notPrimeList:
        continue

    if isPrimeNumber(testNumber):
        primeList.add(testNumber)

        for deleteNumber in numberLIst:
            if deleteNumber % testNumber == 0:
                notPrimeList.add(deleteNumber)
    else:
        numberLIst.remove(testNumber)


print(numberLIst)
print(primeList)
