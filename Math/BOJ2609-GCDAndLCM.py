# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수
import sys
import math
from builtins import print

shortcutInput = sys.stdin.readline


def isPrimeNumber(number):
    for primeNumber in range(2, number):
        if number % primeNumber == 0:
            return False
    return True


def getDivisors(number):
    return list(filter(lambda divisor: number % divisor == 0, [divisor for divisor in range(1, number + 1)]))


def getGCD(firstNumber, secondNumber):
    print(list(filter(isPrimeNumber, getDivisors(firstNumber))))
    # getDivisors(secondNumber)
    pass


def getLCM(firstNumber, secondNumber):
    pass


if __name__ == '__main__':
    firstNumber, secondNumber = map(int, shortcutInput().split())
    print(math.gcd(firstNumber, secondNumber))
    # print(getGCD(firstNumber, secondNumber), getLCM(firstNumber, secondNumber))
