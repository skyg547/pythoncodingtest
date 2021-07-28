# https://www.acmicpc.net/problem/1157
# 단어공부
from collections import  Counter

def solution(strings):
    ansArray = Counter(strings).most_common()
    if ansArray[0][1] is ansArray[1][1]:
        return '?'
    return  str(ansArray[0][0]).upper()

if __name__ == '__main__':

    strings = input()

    if(len(strings) == 1 ):
        print(strings.upper())
        exit()
    countString = dict()

    for chars in strings:

        if chars in countString:
            countString[chars] += 1
        else:
            countString[chars] = 1

    maxValue = max(countString)


    print(solution(strings.lower()))


