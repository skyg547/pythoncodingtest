# https://www.acmicpc.net/problem/1476
# 날자계산

# e 15
# s 28
# m 19

import sys

shortCutInput = sys.stdin.readline
if __name__ == '__main__':

    e, s, m = map(int, shortCutInput().split())
    e, s, m = e % 15, s % 28, m % 19

    a, b, c = 0, 0, 0
    count = 0

    while True:
        count += 1
        a = (a + 1) % 15
        b = (b + 1) % 28
        c = (c + 1) % 19
        if a == e and b == s and c == m:
            break
    print(count)
