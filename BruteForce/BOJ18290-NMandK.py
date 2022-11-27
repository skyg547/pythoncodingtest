# https://www.acmicpc.net/problem/18290
# N과M k
import sys
from itertools import combinations

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1000000


def go(px, py, index, sum):
    if index == k:
        global answer

        if answer < sum:
            answer = sum

        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue

            ok = True
            # 동서남북 방문 했었는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False
                        # 방문
            if ok:
                visited[x][y] = True
                go(x, y, index + 1, sum + arr[x][y])
                visited[x][y] = False


go(0, 0, 0, 0)

print(answer)

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
