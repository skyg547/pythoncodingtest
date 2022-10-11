# https://www.acmicpc.net/problem/4375
# 1
# 1로 이루어진 n의 배수 찾기
#


import sys

shortcutInput = sys.stdin.readline

n = 9901
count = 1

while (True):
    multipleNumber = n*count
    count += 1

    printSet = set()

    strnumber = str(multipleNumber)
    for strs in strnumber:
        if (len(printSet) > 1):
            break
        printSet.add(strs)

    if (len(printSet) > 1) :
        continue
    

    if ('1' in printSet):
        print("succes")
        print(multipleNumber)
        print(len(strnumber))
        break
