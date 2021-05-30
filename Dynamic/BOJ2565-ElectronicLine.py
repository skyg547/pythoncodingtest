# https://www.acmicpc.net/problem/2565
# 전깃줄


# 전깃줄을 없애기


def solution(l):
    # 답을 저장
    ans = 0

    # 정렬을 먼저 시헹
    l.sort()
    print(l)

    subAns = []

    # 차를 저장
    for element in l:
        subAns.append(abs(element[1] - element[0]))

    # 첫번째 숫자가 클 때
    for index in range(1, len(l)):
        if l[index][1] < l[index - 1][1]:
        #     # 둘의 차가 크다면 지워주기

            if subAns[index] < subAns[index - 1]:
                ans += 1
    l.sort(reverse=True)

    for index in range(1, len(l)):
        if l[index][1] < l[index][1]:
            if subAns

    return ans


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
    print(solution(l))
