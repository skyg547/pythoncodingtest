# https://www.acmicpc.net/problem/15652
# N과M 4


from itertools import combinations_with_replacement

if __name__ == '__main__':
    number, repeatCount = map(int, input().split())
    for printValue in list(sorted(combinations_with_replacement(range(1, number + 1), repeatCount, ), key=lambda x: x[0])):
        print(*sorted(printValue))
