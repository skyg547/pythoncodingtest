# https://www.acmicpc.net/problem/15655# N과M 6


from itertools import combinations

if __name__ == '__main__':
    number, repeatCount = map(int, input().split())
    for printValue in list(combinations(sorted(list(map(int, input().split()))), repeatCount)):
        print(*sorted(printValue))
