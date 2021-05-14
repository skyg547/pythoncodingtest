# https://www.acmicpc.net/problem/11659
# 구간 함 구하기 4
import sys

input = sys.stdin.readline


def solution(nl, ml):
    answer = []
    sumArray = [1] * len(nl)

    sumArray[0] = nl[0]
    for element in range(len(nl)):
        if element == 0:
            continue
        else:
            sumArray[element] = sumArray[element - 1] + nl[element]

    for i in ml:
        if (i[0] - 2) == -1:
            answer.append(sumArray[i[1] - 1])
        else:
            answer.append(sumArray[i[1] - 1] - sumArray[i[0] - 2])
    # print(sumArray)
    return answer


if __name__ == '__main__':
    n, m = 5, 3
    nl = [5, 4, 3, 2, 1]
    ml = [[1, 3],
          [2, 4],
          [5, 5]]
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    ml = [list(map(int, input().split())) for _ in range(m)]

    ans = (solution(nl, ml))

    for i in ans:
        print(i)
