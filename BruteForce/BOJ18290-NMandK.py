# https://www.acmicpc.net/problem/18290
# N과M k
import sys
from itertools import combinations

directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}

if __name__ == '__main__':
    rowNumber, colNumber, selectCount = map(int, input().split())
    numberMatrix = []

    for _ in range(rowNumber):
        numberMatrix += list(map(int, input().split()))

    maxSum = -sys.maxsize
    ## 한바퀴 돌면서
    for numbers in list(combinations(numberMatrix, selectCount)):
        ## 이때 두수 인접 했을 시에는 제외 한다
        for numberIndex in range(len(numberMatrix)):  # 인덱스를 돌면서 찾는다
            if numbers[0] == numberMatrix[numberIndex]:  # 첫째수가 같을때
                if numberIndex + 1 < len(numberMatrix):  # n 보다 작고
                    if numbers[1] == numberMatrix[numberIndex + 1]:  # 우측일때
                        continue
                if numberIndex + colNumber < len(numberMatrix):  # n 보다 작고
                    if numbers[1] == numberMatrix[numberIndex + colNumber]:  # n 아래일대
                        continue

                maxSum = max(maxSum, sum(numbers))
    ## 맥스 값을 찾는다
    print(maxSum)
