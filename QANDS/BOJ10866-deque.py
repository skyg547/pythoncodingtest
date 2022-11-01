# # https://www.acmicpc.net/problem/10866
# # # 덱
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다

from collections import deque
import sys

shortcutInput = sys.stdin.readline

if __name__ == '__main__':
    orderCount = int(shortcutInput())
    orders = [shortcutInput().split() for _ in range(orderCount)]

    answerDeque = deque()

    for order in orders:
        if order[0] == 'push_front':
            answerDeque.appendleft(order[1])
        elif order[0] == 'push_back':
            answerDeque.append(order[1])
        elif order[0] == 'size':
            print(len(answerDeque))
        elif order[0] == 'empty':
            print(1 if len(answerDeque) == 0 else 0)
        elif order[0] == 'pop_front' and len(answerDeque) != 0:
            print(answerDeque.popleft())
        elif order[0] == 'pop_back' and len(answerDeque) != 0:
            print(answerDeque.pop())
        elif order[0] == 'front' and len(answerDeque) != 0:
            print(answerDeque[0])
        elif order[0] == 'back' and len(answerDeque) != 0:
            print(answerDeque[-1])
        else:
            print(-1)
