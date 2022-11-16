# https://www.acmicpc.net/problem/15657
# N과M 7


from itertools import combinations_with_replacement

if __name__ == '__main__':
    number, repeatCount = map(int, input().split())
    for printValue in list(combinations_with_replacement(sorted(list(map(int, input().split()))), repeatCount)):
        print(*sorted(printValue))
