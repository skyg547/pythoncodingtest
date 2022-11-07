# https://www.acmicpc.net/problem/1406
# 에디터

from collections import deque
import sys

shortcutInput = sys.stdin.readline


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


if __name__ == '__main__':
    # 값 입력
    initStirng = shortcutInput().strip()
    orderCount = int(shortcutInput())
    orders = [shortcutInput() for _ in range(orderCount)]

    # 초기화
    firstNode = ListNode('')  # 가장 첫노드
    head = firstNode

    for string in initStirng:
        current_node = ListNode(string)
        current_node.prev = head  # 이전노드 설정
        head.next = current_node  # 현재 노드 설정
        head = current_node  # 현재 노드 변경

    # 로직 실행
    for order in orders:
        if order[0] == 'P':
            current_node = ListNode(order[2])
            current_node.prev = head  # 추가하려는 노드 이전 설정
            current_node.next = head.next  # 추가하려는 노드 다음 설정
            head.next = current_node  # 현재 노드의 다음 추가하려는 노드로 설정
            if current_node.next is not None:
                current_node.next.prev = current_node  # 추가하려는 노드
            head = current_node  # 현재 노드 변경
        elif order[0] == 'B' and head is not firstNode:
            head.prev.next = head.next  # 헤드 이전 노드 설정
            if head.next is not None:  # 헤드 다음 노드의 이전 노드 설정
                head.next.prev = head.prev
            head = head.prev
        elif order[0] == 'L' and head is not firstNode:
            head = head.prev
        elif order[0] == 'D' and head.next is not None:
            head = head.next
        anserString = ''

# print(head.val)
anserString = ''

# print all node
node = firstNode
while node:
    print(node.val, end='')
    node = node.next
