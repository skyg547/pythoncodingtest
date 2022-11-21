# https://www.acmicpc.net/problem/10972
# 다음 순열

from itertools import permutations

if __name__ == '__main__':
    number = int(input())
    targetNumberList = list(map(int, input().split()))
    targetList = list(permutations(range(1, number + 1)))
    # for index, upperNumber in enumerate(targetNumberList):
    #   targetList = list(filter(lambda x: x[index] >= upperNumber, targetList))
    for indexs, upperNumbers in enumerate(targetList):
        isTarget = True
        for index, upperNumber in enumerate(targetNumberList):
            if upperNumbers[index] != upperNumber:
                isTarget = False
                break
        if isTarget:
            print(-1) if indexs + 1 == len(targetList) else print(targetList[indexs + 1])
