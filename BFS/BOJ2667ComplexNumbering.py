# 단지번호 붙이기
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	128 MB	80579	33003	20887	39.130%
# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
#
#
# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
#
# 예제 입력 1
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 예제 출력 1
# 3
# 7
# 8
# 9

import sys
from collections import deque

input = sys.stdin.readline

def solution(n, lists):
    ans = []

    # 좌 우 상, 하
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # bfs 수행할 큐
    queue = deque()

    # y 축을 돌고
    for y in range(n):
        # x축을 돌고
        for x in range(n):

            # 0 의 아니면
            if lists[y][x] != 0:
                # 수를 저장합니다. 나중에 비교를 위해
                number = lists[y][x]

                # 크기 측정할 사이즈
                size = 1

                # 큐에 좌표를 추가
                queue.append([y, x])

                # x 방문처리
                lists[y][x] = 0

                # bfs 탐색
                # 큐가 있으면
                while queue:
                    # 큐의 제일 앞 노드를 꺼낸뒤
                    node = queue.popleft()

                    # 사방탐색을 실시
                    for num in range(4):
                        # 좌표가 벽 뚫고 나가는지 체크
                        if 0 <= (node[0] + dx[num]) < n and 0 <= (node[1] + dy[num]) < n:
                            # 현재 도는 수랑 같고 큐 에 없다면
                            if lists[node[0] + dx[num]][node[1] + dy[num]] == number and \
                                    [node[0] + dx[num], node[1] + dy[num]] not in queue:
                                #큐에 넣어주고
                                queue.append([node[0] + dx[num], node[1] + dy[num]])
                                # x 방문처리
                                lists[node[0] + dx[num]][node[1] + dy[num]] = 0
                                #사이즈 키워주고
                                size += 1
                ans.append(size)

    return ans


if __name__ == '__main__':

    n = int(input())
    l = []
    for _ in range(n):
        tmeplist = []
        tempinput = input()
        for i in range(n):
            tmeplist.append(int(tempinput[i]))
        l.append(tmeplist)

    # 오르차순 정렬
    answer = sorted(solution(n, l))

    print(len(answer))

    for answers in answer:
        print(answers)
