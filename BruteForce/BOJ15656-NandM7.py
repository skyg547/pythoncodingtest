# https://www.acmicpc.net/problem/15655# N과M 6


from itertools import product

if __name__ == '__main__':
    number, repeatCount = map(int, input().split())
    for printValue in list(product(sorted(list(map(int, input().split()))), repeat=repeatCount)):
        print(*(printValue))
