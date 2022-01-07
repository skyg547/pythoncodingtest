# https://www.acmicpc.net/problem/15650

from itertools import permutations


def solution(n, m):
    return (list(permutations(range(1, 1 + n), m)))


if __name__ == '__main__':
    n , m = map(int , input().split())
    for element in solution(n,m):
        print(*element)
