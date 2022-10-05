# https://www.acmicpc.net/problem/1037
# 약수
import sys

shortcutInput = sys.stdin.readline


def getAliquot(aliquotList):
    return max(aliquotList) * min(aliquotList)


if __name__ == '__main__':
    aliquotCount = int(shortcutInput())
    aliquotList = sorted(list(map(int, shortcutInput().split())))

    print(getAliquot(aliquotList))
