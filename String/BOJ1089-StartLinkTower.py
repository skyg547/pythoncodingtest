# https://www.acmicpc.net/problem/1089
# # 스타트 링크 타워

from itertools import permutations, product


def solution(n, l):
    s = [[] for _ in range(n)]

    for length, element in zip(range(n), l):
        if element == 0:
            s[length].append(0)
            s[length].append(8)

        elif element == 1:
            s[length].append(1)
            s[length].append(0)
            s[length].append(3)
            s[length].append(4)
            s[length].append(7)
            s[length].append(8)
            s[length].append(9)

        elif element == 2:
            s[length].append(8)
            s[length].append(2)

        elif element == 3:
            s[length].append(3)
            s[length].append(8)
            s[length].append(9)

        elif element == 4:
            s[length].append(4)
            s[length].append(8)
            s[length].append(9)

        elif element == 5:
            s[length].append(5)
            s[length].append(6)
            s[length].append(8)
            s[length].append(9)

        elif element == 6:
            s[length].append(8)
            s[length].append(6)

        elif element == 7:
            s[length].append(0)
            s[length].append(3)
            s[length].append(7)
            s[length].append(8)
            s[length].append(9)

        elif element == 8:
            s[length].append(8)

        elif element == 9:
            s[length].append(8)
            s[length].append(9)
        elif element == 10:
            s[length].append(0)
            s[length].append(1)
            s[length].append(2)
            s[length].append(3)
            s[length].append(4)
            s[length].append(5)
            s[length].append(6)
            s[length].append(7)
            s[length].append(8)
            s[length].append(9)

    # * ->  껍질을 벗겨 낸다!!
    array = (list(product(*s)))
    answerNumer = []
    for i in array:
        string = ''
        for j in i:
            string += str(j)

        answerNumer.append(int(string))
    # print(array)
    # array = (list(map(lambda x: int(str(x[0]) + str(x[1])), permutations(s, n))))
    # print(array)

    # print(s)
    if len(answerNumer) == 0:
        return 0
    return sum(answerNumer) / len(answerNumer)


if __name__ == '__main__':
    # 2
    # .......
    # .......
    # .......
    # .......
    # .......
    #
    # 2
    # ###.###
    # #.#.#.#
    # #.#.###
    # #.#...#
    # ###.###

    n = 2
    l = [0, 9]

    n = int(input())
    l = []

    zero = ['###',
            '#.#',
            '#.#',
            '#.#',
            '###']
    one = ['..#',
           '..#',
           '..#',
           '..#',
           '..#']
    two = ['###',
           '..#',
           '###',
           '#..',
           '###']
    three = ['###',
             '..#',
             '###',
             '..#',
             '###']
    four = ['#.#',
            '#.#',
            '###',
            '..#',
            '..#']
    five = ['###',
            '#..',
            '###',
            '..#',
            '###']
    six = ['###',
           '#..',
           '###',
           '#.#',
           '###']
    seven = ['###',
             '..#',
             '..#',
             '..#',
             '..#']
    eight = ['###',
             '#.#',
             '###',
             '#.#',
             '###']
    nine = ['###',
            '#.#',
            '###',
            '..#',
            '###']
    allnumber = ['...',
                 '...',
                 '...',
                 '...',
                 '...']
    inputnumber = [(input().split()) for _ in range(5)]
    # print(inputnumber)
    for num in range(n):
        tempNumber = []
        if num == 0:
            for x in range(5):
                tempNumber.append(inputnumber[x][0][num] + inputnumber[x][0][num + 1] + inputnumber[x][0][num + 2])
        else:
            for x in range(5):
                tempNumber.append(
                    inputnumber[x][0][(4 * num)] + inputnumber[x][0][(4 * num) + 1] + inputnumber[x][0][(4 * num) + 2])
        # print(tempNumber)
        if tempNumber == zero:
            l.append(0)
        elif tempNumber == one:
            l.append(1)
        elif tempNumber == two:
            l.append(2)
        elif tempNumber == three:
            l.append(3)
        elif tempNumber == four:
            l.append(4)
        elif tempNumber == five:
            l.append(5)
        elif tempNumber == six:
            l.append(6)
        elif tempNumber == seven:
            l.append(7)
        elif tempNumber == eight:
            l.append(8)
        elif tempNumber == nine:
            l.append(9)
        elif tempNumber == allnumber:
            l.append(10)

    if not l:
        print(-1)
        exit()
    # print('llllllll', l)
    print(solution(n, l))

    # n 1 2 3 4 5 6 7 8 9

    ###...#.###.###.#.#.###.###.###.###.###
    # .#...#...#...#.#.#.#...#.....#.#.#.#.#
    # .#...#.###.###.###.###.###...#.###.###
    # .#...#.#.....#...#...#.#.#...#.#.#...#
    ###...#.###.###...#.###.###...#.###.###
# 어떻게 문자열입력?
