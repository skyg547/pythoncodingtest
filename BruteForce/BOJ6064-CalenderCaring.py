# # https://www.acmicpc.net/problem/6064
# # 카잉 달력
#
# M과 N보다 작거나 같은 두 개의 자연수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현
#
# 수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다. 그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다. <x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1
# y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1


# 최소공배수, 숫자 한개 고정
import math
import sys

shortCutInput = sys.stdin.readline


# 최소 공배수 구하기
def getLcm(firstNumber, secondNumber):
    return (firstNumber * secondNumber / math.gcd(firstNumber, secondNumber))


# 해 구하기
def getYear(calender):
    m, n, x, y = calender[0], calender[1], calender[2], calender[3]
    # 숫자 한개 고정 반복 횟수 줄이기
    tempX, tempY = x, n if (x % n == 0) else (x % n)
    year = x
    maxNumber = int(getLcm(m, n))
    # x 부터 +m 개씩 증가, 일치하는 Y 찾기, 마지막해 최소공배수
    while True:
        if tempY == y:
            return year
        year += m
        tempY += m
        if tempY > n:
            tempY = n if (tempY % n == 0) else (tempY % n)  # n 나머지가 다음수, 0 으로 떨어질시 n
        if year > maxNumber:
            return -1


if __name__ == '__main__':
    number = int(shortCutInput())
    testCases = [list(map(int, shortCutInput().split())) for _ in range(number)]

    for testCase in testCases:
        print(getYear(testCase))
