import sys
factorial_memo = {}


def factorial(n):
    if n < 2:
        return 1
    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n - 1)
    return factorial_memo[n]


def solution(n):
    answer = factorial(n)

    cnt = 0

    while 1:
        if answer % 10 == 0:
            answer = answer / 10
            cnt += 1
        else:
            break

    return cnt


sys.setrecursionlimit(10**9)
n = 4294967296
print(solution(n))
