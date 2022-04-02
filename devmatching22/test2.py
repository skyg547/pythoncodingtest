import copy
import itertools


def solution(grid):
    abc = ['a', 'b', 'c']

    for alphabetList in list((itertools.permutations(abc, "".join(grid).count('?')))):
        checkGrid = copy.deepcopy(grid)
        alphalist = list(alphabetList)
        for row in range(len(checkGrid)):
            for col in range(len(checkGrid[row])):
                if checkGrid[row][col] == '?':
                    checkGrid[row].replace('?', alphalist.pop())
        print(checkGrid)
    answer = -1
    # print(grid)
    return answer


if __name__ == '__main__':
    print(solution(["??b", "abc", "cc?"]))
