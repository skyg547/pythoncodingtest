# https://www.acmicpc.net/problem/4375
# 1
# 1로 이루어진 n의 배수 찾기
#

import sys
shortcutInput = sys.stdin.readline
while True:
    try:
        n = int(input())

        number = ''
        while (True):
            number += '1'
            if (int(number) % n == 0):
                print(len(number))
                break

    except:
        break
