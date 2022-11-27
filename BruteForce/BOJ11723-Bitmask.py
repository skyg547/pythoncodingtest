# https://www.acmicpc.net/problem/11723
# 집합

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    number = int(input())
    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    # empty: S를 공집합으로 바꾼다.
    answerSet = set()
    for _ in range(number):
        command = input().split()

        if command[0] == 'add':
            answerSet.add(int(command[1]))
        elif command[0] == 'remove':
            answerSet.discard(int(command[1]))
        elif command[0] == 'check':
            print(1 if int(command[1]) in answerSet else 0)
        elif command[0] == 'toggle':
            if int(command[1]) in answerSet:
                answerSet.remove(int(command[1]))
            else:
                answerSet.add(int(command[1]))
        elif command[0] == 'empty':
            answerSet.clear()
        elif command[0] == 'all':
            answerSet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                         11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
