# https://www.acmicpc.net/problem/25305
# 커트라인

import sys

shortcutInput = sys.stdin.readline


def getCutLine(candidateList, winnerCount):
    return sorted(candidateList, reverse=True)[winnerCount-1:winnerCount:]


if __name__ == '__main__':
    candidate, winnerCount = map(int, shortcutInput().split())

    candidateList = list(map(int, shortcutInput().split()))
    print(*getCutLine(candidateList, winnerCount))
