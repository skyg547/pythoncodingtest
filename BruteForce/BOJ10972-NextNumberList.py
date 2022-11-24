# https://www.acmicpc.net/problem/10972
# 다음 순열


if __name__ == '__main__':
    number = int(input())
    targetNumberList = list(map(int, input().split()))

    for index, upperNumber in enumerate(targetNumberList):
        if index + 1 == number:
            print(-1)
            break
        if targetNumberList[index + 1] < upperNumber:

