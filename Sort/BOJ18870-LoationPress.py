# https://www.acmicpc.net/problem/18870
# 좌표 압축


def solution(lists) :
    answerLists = []
    print()

    for element in lists :
        answerLists.append(sorted(set(lists)).index(element))

    return answerLists

if __name__ == '__main__':
    number = int(input())

    lists = list(map(int, input().split()))
    print(*solution(lists))


