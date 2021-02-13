# 카펫
# 문제 설명
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
#
# carpet.png
#
# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
#
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다. -> 중요조건
# 입출력 예
# brown	yellow	return
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]
def solution(brown, yellow):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow) ** 0.5) / 4)
    y = (brown + yellow) // x

    return [max(x, y), min(x, y)]


def solution(brown, yellow):
    for a in range(1, int(yellow ** 0.5) + 1):
        if not yellow % a:
            b = yellow // a
            if 2 * a + 2 * b + 4 == brown:
                return [b + 2, a + 2]


#  근의 공식을 이용한 풀이
import math
def solution(brown, yellow):
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2,yellow//ans+2]
brown = 10
yellow = 2
print(solution(brown, yellow))
