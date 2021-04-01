from itertools import permutations


def solution(n, s):
    lists = list(map("".join, permutations(s, n)))

    temp = []
    for i in lists:
        if i == ''.join(sorted(i)):
            temp.append(i)
    return temp


# n, s = 4, 6
# ls = ['a', 't', 'c', 'i', 's', 'w']
# print(ls)
ls = []
n, s = map(int,input().split())
# for i in range(int(s)):
#     ls.append(input())
ls = list(input().split())

# print(ls)
for i in solution(n, ls):
    print(i)
