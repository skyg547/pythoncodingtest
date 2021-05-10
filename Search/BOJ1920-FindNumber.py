# https://www.acmicpc.net/problem/1920
# 수찾기


def solution(NL, ML):
    answer = []
    NL.sort()

    start = 0
    end = len(NL)

    for element in ML:
        point = 0
        start = 0
        end = len(NL)-1

        while start <= end:
            mid = (start + end) // 2
            # print(start, end, mid)
            if element == NL[mid]:
                answer.append(1)
                point = 1
                break
            elif element < NL[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if point == 0:
            answer.append(0)

    return answer


if __name__ == '__main__':
    N = 5
    NL = [4, 1, 5, 2, 3]
    M = 5
    ML = [1, 3, 7, 9, 5]
    N = int(input())
    NL = list(map(int, input().split()))
    M = int(input())
    ML = list(map(int, input().split()))
    ans = (solution(NL, ML))

    for ele in ans:
        print(ele)

