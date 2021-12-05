# https://www.acmicpc.net/problem/18870
# 좌표 압축
# sortedList.index(element) o(n) 시간 복잡도

import sys

input = sys.stdin.readline

def solution(lists) :
    answerLists = []
    sortedList = sorted(set(lists))
    sortedDict = {sortedList[i] : i for i in range(len(sortedList))}

    #print(sortedDict)
    for element in lists :
        answerLists.append(sortedDict[element])

    return answerLists

if __name__ == '__main__':
    number = int(input())

    lists = list(map(int, input().split()))
    print(*solution(lists))


