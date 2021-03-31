from itertools import combinations


def solution(s, m):
    min = m
    for i in list(combinations(s, 3)):
        if sum(i) <= m:
            if min > abs(m - sum(i)):
                min = abs(m - sum(i))

    return abs(m - min)


n, m = map(int, input().split())
s = list(map(int, input().split()))
print(solution(s, m))
