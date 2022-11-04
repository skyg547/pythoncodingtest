# https://www.acmicpc.net/problem/9012
# 괄호

if __name__ == '__main__':
    count = int(input())
    parentheises = [list(input()) for _ in range(count)]

    for parentheis in parentheises:
        parentheisStack = []
        for strings in parentheis:
            if len(parentheisStack) != 0 and strings != parentheisStack[-1] and strings == ')':
                parentheisStack.pop()
                continue
            parentheisStack.append(strings)

        if len(parentheisStack) == 0:
            print('YES')
        else:
            print('NO')
