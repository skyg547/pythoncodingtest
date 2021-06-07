# https://www.acmicpc.net/problem/2293
# 동전 1
import sys

input = sys.stdin.readline

def solution(l, k):


    #   1 2 3 4 5 6 7 8 9 10
    # 1 1 1 1 1 1 1 1 1 1 1
    # 2 0 1 1 2 2 3 3 4 4 5
    # 5 0 2 2 3 4 5 5 7 8 10

    # 2, 6 일때 1 ,6 + 2,4 하는거랑 같다
    # 각 동전을 저장할 배열
    answerArray = [0] * (k + 1)

    # 0원을 쓰는 경우는 아무 것도 안쓰는거 1가지라 초기화 하였다
    answerArray[0] = 1
    # print(answerArray)

    # 각 배열을 도는데 점화식을 통하면 위 그림처럼 된다.
    for element in l:
        for index2 in range(element, k + 1):
            answerArray[index2] += answerArray[index2 - element]

    # 2을 의 경우
    # 3의경우

    return answerArray[k]


if __name__ == '__main__':
    n, k = map(int, input().split())

    l = [int(input()) for _ in range(n)]
    print(solution(l, k))
