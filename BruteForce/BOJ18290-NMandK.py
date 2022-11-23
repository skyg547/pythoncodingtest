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

    ## 모든 경우 다 구해주기
    print(numberMatrix)

    maxSum = -sys.maxsize
    numberIndex = -1
    lastNumber = -100002
    ## 한바퀴 돌면서
    for numbers in list(combinations(numberMatrix, selectCount)):
        if(lastNumber != ):
            numberIndex++
        ## 이때 두수 인접 했을 시에는 제외 한다 1. 우측 일때 +1 인덱스. 2 아래 일때 + m  , 길이가 넘어 n 을 넘으면 안된다 .
        if (numbers[0] == 9 and numbers[1] == 8) or \
                (numbers[0] == 9 and numbers[1] == 8):
            continue
        maxSum = max(maxSum, sum(numbers))
    ## 맥스 값을 찾는다
    print(maxSum)

# for index, numbers in enumerate(list(combinations(numberMatrix, selectCount))):
#     if index % (23) == 0:
#         print()
#     print(numbers, index)
# for rowindex, row in enumerate(numberMatrix):
#     for colindex, col in enumerate(row):
#         for selectrowindex, row in range(rowindex, rowNumber+1 ):
#             for colindex, col in range(colindex, colNumber+1 ):
#                 for direction in directions:
#
#                 print(rowindex, colindex)
#                 print(row,col)
# 여태까지 인덱스 제게

# for indexs in range(rowNumber * colNumber):
#     for doubleindexs in range((rowNumber * colNumber) - indexs):
#         print(indexs + doubleindexs)
#
# for indexs in range(rowNumber * colNumber):
#     for doubleindexs in range((rowNumber * colNumber) - indexs):
#         print(indexs + doubleindexs)
