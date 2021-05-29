# https://www.acmicpc.net/problem/10815
# 숫자 카드


# bisect 라이브러리 (이분 탐색 라이브러리 )
# index 함수 쓰면 시간 초과 순차 탐색이라 그런거 같다
def solution(nl, ml):
    # 정답 배열
    answer = [0] * (len(ml))

    # 배열 정렬
    nl.sort()

    # 원소를 돌면서
    for element in range(len(ml)):
        left = 0
        right = len(nl)-1

        #왼쪽이 더 작을때만 반복을 하는데
        while left <= right:
            # 중앙값은 왼쪽 오른쪽 더해서 나누고
            mid = (left + right) // 2

            # 만약 그값과 일치한다면
            if nl[mid] == ml[element]:
                # 인덱스를 조정해주고
                answer[element] = 1
                # 탈출
                break

            # 중압값 보다 크면 오른쪽 작게
            elif nl[mid] > ml[element]:
                right = mid - 1
            # 왼쪽 더해주기
            else:
                left = mid + 1


    # # 원소를 돌면서
    # for element in ml:
    #
    #     a = 0
    #     b = len(nl) // 2 - 1
    #     # 엘리 먼트가 중앙 값보다 작으면
    #     if element < nl[len(nl) // 2]:
    #         # 앞쪽만 돈다
    #         for i in range(a, len(nl) // 2):
    #             if nl[i] == element:
    #                 answer[ml.index(element)] = 1
    #                 a = i
    #                 break
    #     else:
    #         for i in range(b, len(nl)):
    #             if nl[i] == element:
    #                 answer[ml.index(element)] = 1
    #                 b = i
    #                 break

    return answer


if __name__ == '__main__':
    N = 5
    Nl = [6, 3, 2, 10, - 10]
    M = 8
    Ml = [10, 9, - 5, 2, 3, 4, 5, - 10]

    N = input()
    Nl = list(map(int, input().split()))
    M = input()
    Ml = list(map(int, input().split()))

    print(*solution(Nl, Ml))
