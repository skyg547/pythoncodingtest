# https://www.acmicpc.net/problem/18870
# 좌표 압축

import sys

input = sys.stdin.readline

def solution(lists) :
    answerLists = []
    sortedList = sorted(set(lists))

    for element in lists :
        answerLists.append(sortedList.index(element))

    return answerLists

if __name__ == '__main__':
    number = int(input())

    lists = list(map(int, input().split()))
    print(*solution(lists))


