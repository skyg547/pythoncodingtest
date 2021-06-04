# https://www.acmicpc.net/problem/12852
# 1로 만들기 버전 2

import sys


def solution(n):
    answer1 = 1e9
    answer2 = [0]
    cnt = 0

    while n != 1:
        cnt += 1
        if n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1

    # 1일때 그전 결과 값이랑 비교
    if n == 1:
        answer1 = min(answer1, cnt)
        return answer1


if __name__ == '__main__':
    print(solution(10))

# 3
# 10  9 3 1
