# https://www.acmicpc.net/problem/1748
# 수 이어 쓰기1
#
# 12345
# 123456789 10 11

# 1 10 100 1000 10000
# 10 99

import sys

shortCutInput = sys.stdin.readline
if __name__ == '__main__':

    number = int(shortCutInput())
    divideNumber = 1
    numberLength = 1
    answer = 0
    count = 0

    # 10 자리수 이전 까지 더해주기  ex 154 일때 9*1 + 90*2
    while number // divideNumber > 9:
        answer += (((divideNumber * 10) - divideNumber) * numberLength)
        numberLength += 1
        divideNumber *= 10

    answer += (number - divideNumber + 1) * numberLength  # 자기 자신 + (자리수 까지 포합 +1)  - 자릿수 * 문자 갯수
    print(answer)
