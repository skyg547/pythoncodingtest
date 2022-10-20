# https://www.acmicpc.net/problem/3085
# 사탕겡미

# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 방법 1
# 1. 동서남북으로 다 바꿔 본다
# 2. 가장긴 배열을 검사 한다
#
# 방법 2
# 1. 가장 긴 배열을 찾는다
# 2. 주변에 같은 문자가 있는지 찾는다

# 1.사탕의 색이 다른 인접한 두 칸을 고른다
# 2.서른 칸에 들어있는 사탕을 서로 교환한다
# 3.모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다

# 동서남북 검사 자기 행, 열만 검사
# 자기 행, 자기 열 가장 긴 문자열 값 찾기

import sys

shortCutInput = sys.stdin.readline

directionLiset = [(-1, 0),  # 북
                  (0, -1),  # 서
                  (1, 0),  # 남
                  (0, 1)]  # 동


def getMaxLengthAlphabet(string):
    maxLengthAplpha = ''
    for alphaIndex in range(len(string)):
        tempAlphabet = ''
        for alphaIndex2 in range(alphaIndex, len(string)):
            if string[alphaIndex] == string[alphaIndex2]:
                tempAlphabet += string[alphaIndex2]
            else:
                break

        if len(maxLengthAplpha) < len(tempAlphabet):
            maxLengthAplpha = tempAlphabet
    return maxLengthAplpha


def swapTheList(lists, firstLocation, secondLocation):
    tempValue = lists[firstLocation[0]][firstLocation[1]]
    lists[firstLocation[0]][firstLocation[1]] = lists[secondLocation[0]][secondLocation[1]]
    lists[secondLocation[0]][secondLocation[1]] = tempValue
    return lists


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    # lists = [list('CCP'),
    #          list('CCP'),
    #          list('PPC')]
    lists = [list(sys.stdin.readline()) for _ in range(n)]

    maxLengthString = ''

    # 모든 리스트를 순회
    for row in range(n):
        for col in range(n):
            ### 자기 자신 최대 길이 부터 구하기
            # 행열 변경 리스트
            tempList = list(zip(*lists))
            # 행 최대 길이
            rowMaxLengthAlpha = getMaxLengthAlphabet(''.join(lists[row]))
            # 열 최대 길이
            colMaxLengthAlpha = getMaxLengthAlphabet(''.join(tempList[col]))

            # 최대 문자 구하기
            if len(maxLengthString) < len(rowMaxLengthAlpha):
                maxLengthString = rowMaxLengthAlpha
            if len(maxLengthString) < len(colMaxLengthAlpha):
                maxLengthString = colMaxLengthAlpha

            for direction in directionLiset:
                # 바뀌는 방향 좌표 구해주기
                changedRow = row + direction[0]
                changedCol = col + direction[1]
                if changedRow < 0 or changedCol < 0 or changedRow == n or changedCol == n:  # 밖으로 나갔는지 안나갔는지 검사
                    continue

                if lists[row][col] == lists[changedRow][changedCol]:
                    continue

                # 문자 바꿔 주기
                swapTheList(lists, (row, col), (changedRow, changedCol))
                # 행열 변경 리스트
                tempList = list(zip(*lists))
                # 행 최대 길이
                rowMaxLengthAlpha = getMaxLengthAlphabet(''.join(lists[row]))
                # 열 최대 길이
                colMaxLengthAlpha = getMaxLengthAlphabet(''.join(tempList[col]))

                # 최대 문자 구하기
                if len(maxLengthString) < len(rowMaxLengthAlpha):
                    maxLengthString = rowMaxLengthAlpha
                if len(maxLengthString) < len(colMaxLengthAlpha):
                    maxLengthString = colMaxLengthAlpha

                # 행열  원상 복구
                swapTheList(lists, (row, col), (changedRow, changedCol))
    print(len(maxLengthString))
