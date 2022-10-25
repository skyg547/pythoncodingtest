# https://www.acmicpc.net/problem/1107
# 리모컨
#
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다.
# +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
# -를 누르면 -1된 채널로 이동한다.
# 채널 0에서 -를 누른 경우에는 채널이 변하지 않고,
# 채널은 무한대 만큼 있다.
#
#
# 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러
# first N = 100
# (0 ≤ N ≤ 500,000)
# M(0 ≤ M ≤ 10)
from itertools import product
import sys

shortCutInput = sys.stdin.readline
if __name__ == '__main__':
    nowChannel = 100
    targetChannel = str(int(shortCutInput()))
    errorButtonCount = int(shortCutInput())
    errorButtons = []
    if errorButtonCount != 0:
        errorButtons = list(map(int, shortCutInput().split()))
    pressButtonCount = 0
    if nowChannel == int(targetChannel):
        print(0)
        exit()

    targetNumberSet = set(list(targetChannel))
    pressButtonList = list()  # 가까운 버튼 리스트

    # 가장 가까운 버튼 리스트 구하기
    for index, button in enumerate(targetChannel):
        getNextToNumber = 0
        while len(pressButtonList) != index + 1:
            nextToNumberList = set()
            plusNumber = int(button) + getNextToNumber
            minusNumber = int(button) - getNextToNumber

            if plusNumber not in errorButtons and plusNumber < 10:
                nextToNumberList.add(int(button) + getNextToNumber)
            if minusNumber not in errorButtons and minusNumber > -1:
                nextToNumberList.add(int(button) + getNextToNumber)

            if len(nextToNumberList) != 0:
                pressButtonList.append(nextToNumberList)
                break

            getNextToNumber += 1

    # 가능한 모든 버튼리스트 구하기
    # print(list(product(*list(pressButtonList))))
    # setList = list(map(lambda x: ''.join(),  (list(product(*pressButtonList)))))
    setList = [''.join(map(str, i)) for i in list(product(*pressButtonList))]

    # print(((6, 6, 6).values()))
    minNumber = min(setList, key=lambda x: abs(int(x) - int(targetChannel)))
    print(minNumber)
    print(abs(int(minNumber) - int(targetChannel)) + len(minNumber))

    # for sets in setList:
    #     print(tasets)
