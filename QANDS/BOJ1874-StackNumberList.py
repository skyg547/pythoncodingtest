# https://www.acmicpc.net/problem/1874
# 스택 수열


if __name__ == '__main__':
    n = int(input())
    numberList = [int(input()) for _ in range(n)]
    stackUse = [False for _ in range(n + 1)]

    stackNumberList = [0]
    printList = []
    # 숫자 반복
    for number in numberList:
        while stackNumberList[-1] != number:
            # pop 할 숫자가 있는지 여부 체크
            # 작은지 큰지 여부
            if stackNumberList[-1] < number:  # 작을때 push
                # 스택 push 여부 체크
                if stackUse[stackNumberList[-1] + 1]:
                    print("NO")
                    print(number)
                    print(stackUse)
                    exit()
                stackUse[stackNumberList[-1] + 1] = True  # push 사용 체크
                stackNumberList.append(stackNumberList[-1] + 1)  # 스택 push
                printList.append('+')  # push 출력
            elif stackNumberList[-1] > number:
                if stackUse[stackNumberList[-1] - 1] == 0:  # pop 없는지 체크
                    print("NO")
                    print(number)
                    exit()
                stackNumberList.pop()  # 스택 push
                printList.append('-')  # pop 출력

    for printValue in stackUse:
        if printValue == 0:
            continue
        print(printValue)
