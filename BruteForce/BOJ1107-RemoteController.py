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

    # 가장 작은 횟수 카운트
    minNumber = sys.maxsize

    # 모든 숫자 돌아 보기
    for i in range(5000001):
        # 버튼 클릭 가능 여부 확인
        canButton = True
        for stirngs in list(str(i)):
            if int(stirngs) in errorButtons:
                canButton = False
                break
        # +,- 가는 횟수 구하기
        tempMinNumber = abs(int(targetChannel) - 100)
        # 숫자 +,- 가는 횟수 구하기
        if canButton:
            # 더 작은 것 출력
            tempMinNumber = min(len(str(i)) + abs(int(i) - int(targetChannel)), tempMinNumber)
        #  현재 가장 작은 횟수와 비교
        minNumber = min(tempMinNumber, minNumber)
    print(minNumber)
