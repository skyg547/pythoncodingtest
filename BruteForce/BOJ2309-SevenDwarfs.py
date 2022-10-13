# https://www.acmicpc.net/problem/2309
# 일곱난쟁이

import sys

shortCutInput = sys.stdin.readline

def findFakeDwarfs(dwarfs, height):
    heightOfDwarfs = sum(dwarfs)
    for fakeDwarf1 in dwarfs:
        for fakeDwarf2 in dwarfs:
            if heightOfDwarfs - fakeDwarf2 - fakeDwarf1 == height:
                return [fakeDwarf1, fakeDwarf2]


if __name__ == '__main__':
    dwarfsCount = 9
    dwarfs = sorted([int(shortCutInput()) for _ in range(dwarfsCount)])

    for fakeDwarfs in findFakeDwarfs(dwarfs, 100):
        dwarfs.remove(fakeDwarfs)

    for dwarf in dwarfs:
        print(dwarf)




