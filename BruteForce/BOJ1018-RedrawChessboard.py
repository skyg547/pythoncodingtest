# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

# 스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
#  8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했
# 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램
def solution(l, type1, type2):
    minimum = 0

    for index, element in enumerate(l):
        #        print(index, element)
        for index2, element2 in enumerate(element):
            if type1[index][index2] is not element2:
                minimum += 1

    return minimum


if __name__ == '__main__':
    n = 8
    m = 8
    l = ['WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBBBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW']

    type1 = ['WBWBWBWB',
             'BWBWBWBW',
             'WBWBWBWB',
             'BWBWBWBW',
             'WBWBWBWB',
             'BWBWBWBW',
             'WBWBWBWB',
             'BWBWBWBW']

    type2 = [
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB'
    ]

    returnValue = solution(l, type1, type2)
    print(returnValue)