# https://www.acmicpc.net/problem/2675
# 문자열 반복

def solution():
    n = input()

    for _ in range(int(n)):
        stringList = list(input().split())

        tempAnswer =''
        for element in stringList[1]:
            for number in range(int(stringList[0])):
                tempAnswer += element
        print(tempAnswer)

if __name__ == '__main__':
    solution()