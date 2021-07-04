# https://www.acmicpc.net/problem/2468
# 안전 영역

def solution(l):

    rainHeight = 0
    #비 최대 높이 구하기
    for maxElement in l:
        if rainHeight < max(maxElement):
            rainHeight = max(maxElement)




    return


if __name__ == '__main__':
    s = 5
    l = [[6, 8, 2, 6, 2],
         [3, 2, 3, 4, 6],
         [6, 7, 3, 3, 2],
         [7, 2, 5, 3, 6],
         [8, 9, 5, 2, 7]]
    print(solution(l))
