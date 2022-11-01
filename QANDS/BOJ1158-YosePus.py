# https://www.acmicpc.net/problem/1158
# 요세푸스문제

from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    yosepus = deque(range(1, n + 1))
    printValue = '<'
    while True:
        for _ in range(k - 1):
            yosepus.append(yosepus.popleft())
        printValue += str(yosepus.popleft())
        if len(yosepus) == 0:
            printValue += '>'
            break
        printValue += ', '
    print(printValue)