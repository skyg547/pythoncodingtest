# https://www.acmicpc.net/problem/1406
# 에디터

from collections import deque
import sys

shortcutInput = sys.stdin.readline


def executeOrder(order, string, cursorIndex):
    if order[0] == 'P':
        string.insert(cursorIndex, order[2])
        cursorIndex += 1
    elif order[0] == 'B' and cursorIndex != 0:
        del string[cursorIndex - 1]
        cursorIndex -= 1
    elif order[0] == 'L' and cursorIndex != 0:
        cursorIndex -= 1
    elif order[0] == 'D' and cursorIndex != len(string):
        cursorIndex += 1

    return string, cursorIndex


if __name__ == '__main__':
    initStirng = shortcutInput()
    orderCount = int(shortcutInput())
    orders = [shortcutInput() for _ in range(orderCount)]
    string = deque(initStirng.strip())
    cusorIndex = len(string)

    for order in orders:
        string, cusorIndex = executeOrder(order, string, cusorIndex)

    print(''.join(string))
