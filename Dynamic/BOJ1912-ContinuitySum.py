# https://www.acmicpc.net/problem/1912
# 연속합


# 덱 으로 구현

from collections import deque


def solution(l):
    x = deque()
    answer = [l[0]]
    # 일단 모든 순서의함을 순차대로 도는데
    for i in range(len(l) - 1):
        # 지금과 다음값 더한거 큰걸 넣어주냐 or 새로운 값이 더큰걸 넣어주냐
        answer.append(max(answer[i] + l[i + 1], l[i + 1]))

    #가장 큰값을 반환해준다
    return max(answer)



if __name__ == '__main__':
    s = 10
    l = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

    s = int(input())
    l = list(map(int, input().split()))
    print(solution(l))
