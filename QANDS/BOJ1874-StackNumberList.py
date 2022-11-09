# https://www.acmicpc.net/problem/1874
# 스택 수열


if __name__ == '__main__':
    n = int(input())
    numberList = [int(input()) for _ in range(n)]
    inputNumberList = list(range(1, n + 1))[::-1]
    stackNumberList = [0]
    printList = []
    # 숫자 반복
    for number in numberList:
        while True:
            # pop 할 숫자가 있는지 여부 체크
            # 작은지 큰지 여부
            if stackNumberList[-1] < number:  # 작을때 push
                # 스택 push 여부 체크
                stackNumberList.append(inputNumberList.pop())  # 스택 push
                printList.append('+')  # push 출력
            else:
                if stackNumberList[-1] == number:
                    stackNumberList.pop()  # 스택 push
                    printList.append('-')  # push 출력
                    break
                else:
                    print("NO")
                    exit()
    for printValue in printList:
        if printValue == 0:
            continue
        print(printValue)
