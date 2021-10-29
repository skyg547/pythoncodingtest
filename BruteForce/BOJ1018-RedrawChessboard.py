# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

# 스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
# 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했
# 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램
def solution(l, type1, type2):
    minimum = 0
    tempMinmum = 10e2

    # l의 줄의 8 번째 인덱스 까지만 돌기

    # 첫 줄 돌기
    for index, element in enumerate(l):
        if index > 7:
            break
        #  각각 인덱스 비교       print(index, element)
        for index2, element2 in enumerate(element):
            if index2 > 7:
                break
            # 정답이랑 다른지 비교
            if type1[index][index2] is not element2:
                minimum += 1
    # 더작은 것으로 적용
    if tempMinmum > minimum:
        tempMinmum = minimum


    for index, element in enumerate(l):
        #        print(index, element)
        if index2 > 7:
            break
        for index2, element2 in enumerate(element):
            if index > 7:
                break
            if type2[index][index2] is not element2:
                minimum += 1
    if tempMinmum > minimum:
        tempMinmum = minimum

    return tempMinmum


if __name__ == '__main__':
    n = 10
    m = 13

    l = [
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB',
        'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']

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
