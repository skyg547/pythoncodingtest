# https://www.acmicpc.net/problem/15651
# N과M 3


from itertools import product

if __name__ == '__main__':
    number, repeatCount = map(int, input().split())
    for printValue in list(product(range(1, number + 1), repeat=repeatCount)):
        print(*printValue)
