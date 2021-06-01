# https://www.acmicpc.net/problem/2565
# 전깃줄


# 전깃줄을 없애기


def solution(l):
    # 답을 저장
    ans = 0

    # 정렬을 먼저 시헹
    l.sort()
    print(l)

    # 실패 오답
    # subAns = []
    # #
    # # 차를 저장
    # for element in l:
    #     subAns.append(abs(element[1] - element[0]))
    # 실패한 오답
    # # 첫번째 숫자가 클 때
    # for index in range(1, len(l)):
    #     if l[index][1] < l[index - 1][1]:
    #     #     # 둘의 차가 크다면 지워주기
    #
    #         if subAns[index] < subAns[index - 1]:
    #             ans += 1
    # l.sort(reverse=True)
    #
    # for index in range(1, len(l)):
    #     if l[index][1] < l[index][1]:
    #         if subAns
    #

    #LIS로 풀이

    # LIS를 구해주자
    result = [[] for _ in range(len(l))] # LIS 담을 배렬

    # 각 원소 마다 돌면서
    for i in range(len(l)):
        # 맨 처음은 하나
        if i == 0:
            result[i].append(l[i][1])
        # 아니면
        else:
            # i 까지 돌아보면서
            for j in range(0, i):
                # 만약 최장거리 배열이 최근 값보다 크고
                if result[j][-1] < l[i][1]:
                    #
                    if len(result[i]) - 1 < len(result[j]):
                        result[i] = result[j] + [l[i][1]]
            # 아무것도 없다면
            if not result[i]:
                result[i].append(l[i][1])
    for i in range(len(l)):
        ans = max(ans, len(result[i]))

    return len(l)-ans


if __name__ == '__main__':
    s = 8
    l = [[1, 8],
         [3, 9],
         [2, 2],
         [4, 1],
         [6, 4],
         [10, 10],
         [9, 7],
         [7, 6]]

    # s = int(input())
    # l = [list(map(input().split())) for _ in range(s)]
    print(solution(l))
