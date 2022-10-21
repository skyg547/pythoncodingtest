# https://www.acmicpc.net/problem/15650

from itertools import permutations
from itertools import combinations


def solution(n, m):
    return (list(combinations(range(1, 1 + n), m)))


if __name__ == '__main__':
    n, m = map(int, input().split())
    for element in solution(n, m):
        print(*element)
