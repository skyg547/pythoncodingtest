# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수
import math
import sys

shortcutInput = sys.stdin.readline


def getLcm(firstNumber, secondNumber):
    return (firstNumber * secondNumber // math.gcd(firstNumber, secondNumber))


if __name__ == '__main__':
    firstNumber, secondNumber = map(int, shortcutInput().split())
    print(math.gcd(firstNumber, secondNumber))
    print(getLcm(firstNumber, secondNumber))
