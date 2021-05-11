# https://www.acmicpc.net/problem/9372
# 상근이의 여행

import sys
input = sys.stdin.readline

#1 시기 input 시간초과
#2 시기 모든
def solution(N, L):
    answer = [0] * (N + 1)

    cnt = 0
    for element in L:
        if answer[element[0]] == 0 or answer[element[1]] == 0:
            answer[element[0]] = 1
            answer[element[1]] = 1
            cnt += 1

    return cnt


if __name__ == '__main__':
    # 2
    # N, M = 3, 3
    # L = [[1, 2],
    #      [2, 3],
    #      [1, 3]]
    #
    # print(solution(N, L))
    ans= []
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        L = [list(map(int, input().split())) for _ in range(M)]

        ans.append(solution(N, L))
        #ans.append(N-1) 이 정답
    for i in ans:
        print(i)
# 5    4
# 2    1
# 2    3
# 4    3
# 4    5
