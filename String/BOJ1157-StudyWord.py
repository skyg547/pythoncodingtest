# https://www.acmicpc.net/problem/1157
# 단어공부
from collections import Counter


def solution(strings):
    ansArray = Counter(strings).most_common()
    if ansArray[0][1] is ansArray[1][1]:
        return '?'
    return str(ansArray[0][0]).upper()


if __name__ == '__main__':

    strings = input().lower()

    if (len(strings) == 1):
        print(strings.upper())
        exit()
    countString = dict()

    for chars in strings:

        if chars in countString:
            countString[chars] += 1
        else:
            countString[chars] = 1

    maxValue = max(countString.values())
    count = 0

    for countElement in countString.values():

        if countElement == maxValue:
            count += 1

        if count == 2:
            print("?")
            exit()

    for element in countString.items():
        if maxValue ==element[1]:
            print(element[0].upper())
            break

    # print(solution(strings.lower()))
