# https://www.acmicpc.net/problem/1463
# 1로 만들기


if __name__ == '__main__':

    number = int(input())  # target
    makeOneCounts = [0] * (number + 1)  # memozation numbers
    # get min count on make one list
    for tempNumber in range(2, number + 1):
        makeOneCounts[tempNumber] = makeOneCounts[tempNumber - 1] + 1  # 1 을 더했을때 횟수
        # 3의 배수일때
        if tempNumber % 3 == 0:
            makeOneCounts[tempNumber] = min(makeOneCounts[tempNumber // 3] + 1, makeOneCounts[tempNumber])
        # 2의 배수일때
        if tempNumber % 2 == 0:
            makeOneCounts[tempNumber] = min(makeOneCounts[tempNumber // 2] + 1, makeOneCounts[tempNumber])

    print(makeOneCounts[number])
