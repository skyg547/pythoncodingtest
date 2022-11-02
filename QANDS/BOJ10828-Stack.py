# https://www.acmicpc.net/problem/10828
# 스택
# push X: 정수 X를 스택에 넣는 연산이다.pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.size: 스택에 들어있는 정수의 개수를 출력한다.empty: 스택이 비어있으면 1, 아니면 0을 출력한다.top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다

import sys

shortcutInput = sys.stdin.readline


def solution(arr):
    stacks = []
    for command in arr:
        commands = command.split()
        if 'push' == commands[0]:
            stacks.append(commands[1])
        elif 'size' == commands[0]:
            print(len(stacks))
        elif commands[0] == 'pop' and len(stacks) != 0:
            print(stacks.pop())
        elif commands[0] == 'top' and len(stacks) != 0:
            print(stacks[-1])
        elif commands[0] == 'empty':
            if len(stacks) == 0:
                print(1)
            else:
                print(0)
        else:
            print(-1)


i = int(shortcutInput())

arr = [shortcutInput() for _ in range(i)]
solution(arr)
