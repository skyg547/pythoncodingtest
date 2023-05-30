from itertools import combinations


def solution(s):
    answer = 0
    sets = set()
    for i in range(1, len(s)):
        temp = list(map(''.join, combinations(s, i)))
        for j in temp:
            sets.add(j)
    print(sets)

    tempremove = set()
    # 겹치는거 제게
    for i in sets:
        temptrue = True

        for j in range(len(i)):

            for k in range(len(i)):

                if i[j] == i[k]:
                    if j != k:
                        tempremove.add(i)
                        temptrue = False
                        break

            if not temptrue:
                break

    for i in tempremove:
        if i in sets:
            sets.remove(i)

    print(sets)

    tempanswer = []
    for i in range(len(s)):
        print(s[i:])
        print(s[-i:])
        tempanswer.append(s[i:])
    return answer


def solution(n):
    answer = 0
    sets = set()
    for i in range(len(n)):
        temp = ""
        for j in range(len(n)):
            # print(i, j)
            # print(n[j::i+1])
            # print(n[-j::i+1])
            sets.add(n[j:j+i+1:])
            sets.add(n[-j:-j-i-1:])
        # for k in range(i + 1):
    # print(n[i])
    tempremove = set()
    # 겹치는거 제게
    for i in sets:
        temptrue = True

        for j in range(len(i)):

            for k in range(len(i)):

                if i[j] == i[k]:
                    if j != k:
                        tempremove.add(i)
                        temptrue = False
                        break

            if not temptrue:
                break

    for i in tempremove:
        if i in sets:
            sets.remove(i)

    # print(sets)
    # print(sets)
    sets.remove('')
    answer = len(sets)
    return answer


# a, ab ,aba,
s = "zxzxz"
print(solution(s))
