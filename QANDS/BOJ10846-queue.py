# problem
# # 큐
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys

shortcutInput = sys.stdin.readline

if __name__ == '__main__':
    orderCount = int(shortcutInput())
    orders = [shortcutInput().split() for _ in range(orderCount)]

    answerDeque = deque()

    for order in orders:
        if order[0] == 'push':
            answerDeque.append(order[1])
        elif order[0] == 'pop' and len(answerDeque) != 0:
            print(answerDeque.popleft())
        elif order[0] == 'size':
            print(len(answerDeque))
        elif order[0] == 'empty':
            print(1 if len(answerDeque) == 0 else 0)
        elif order[0] == 'front' and len(answerDeque) != 0:
            print(answerDeque[0])
        elif order[0] == 'back' and len(answerDeque) != 0:
            print(answerDeque[-1])
        else:
            print(-1)
