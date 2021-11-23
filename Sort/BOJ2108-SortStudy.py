# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오

from collections import Counter
import sys

input = sys.stdin.readline

def solution(arrayOfNumber):
    arrayOfNumber.sort()
    print(round(sum(arrayOfNumber) / len(arrayOfNumber)))
    print(arrayOfNumber[int((len(arrayOfNumber)-1) / 2)])
    c = Counter(arrayOfNumber).most_common()
    print(max(c, key = lambda  x: x[1]))
    print(c)
    if len(c) != 1:
      print(c[1][0])
    else :
      print(c[0][0])
    print(arrayOfNumber[-1] - arrayOfNumber[0])


n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

solution(arr)
