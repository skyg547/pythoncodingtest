# https://www.acmicpc.net/problem/15650

from itertools import permutations


def solution(n, m):
    return (list(permutations(range(1, 1 + n), m)))


if __name__ == '__main__':
    for element in solution(4, 2):
        print(*element)
