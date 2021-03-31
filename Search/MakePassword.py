from itertools import permutations


def solution(n, s):
    print(set(list(sorted(map(''.join, permutations(s, n))))))

    return 0


n, s = 4, 6
ls = ['a', 't', 'c', 'i', 's', 'w']

print(solution(n, ls))
