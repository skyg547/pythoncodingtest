# # 나이트의 이동
# # 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# # 1 초	256 MB	24097	11503	8649	47.059%
# # 문제
# # 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
# #
# #
# #
# # 입력
# # 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# #
# # 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
# #
# # 출력
# # 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
#
# # 나이트의 이동가능 경로
#
# # 깊이가 너무 깊어 bfs 로 풀어야 한다 .
# import sys
#
#
#
#
# def dfs(l, x, y):
#     if x[0] < 0 and x[1] < 0:
#         return
#     if x[0] >= l and x[1] >= l:
#         return
#     if (x[0] - y[0]) == 0 and (x[1] - y[1]) == 0:
#         return
#     for index in range(8):
#         dfs(l, [x[0] + dx[index], x[1] + dy[index]], y)
#         counts += 1
#
#
# def solution(l, x, y):
#     # 가장 작은값 찾기;
#     answerlist = []
#     global counts
#
#     counts = 0
#
#     dfs(l, x, y)
#
#     return counts
#
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def solution(l, x, y):
    # print(x, y)
    # 일단 bfs 로 돌면서 각 최소값들을 체크해서 판을 모두 채우자
    # 그러면 방문한 곳은 0 이 아닌 만들어 주자

    # 일단 판을 만들고
    gamMap = [[-1] * l for i in range(l)]

    # for index in gamMap:
    #     for element in range(l):
    #         index.append(-1)

    # 게임 맵이 -1 이 아니면
    # bfs 수행
    queue = deque()
    # 시작점 넣기
    queue.append(x)
    # 시작 점 방문 처리
    gamMap[x[0]][x[1]] = 0
    # print(queue)
    # 이동 횟수
    cnt = 0
    move = 0
    tempmove = 0
    # bfs
    while queue[0] != y:
        # 큐에서 지금 위치 꺼내기
        location = queue.popleft()

        for index in range(8):
            # 게임판 을 벗어나는지 체크하기
            if 0 <= location[0] + dy[index] < l and 0 <= location[1] + dx[index] < l:
                # 만약에 방문이 안된곳이라면
                if gamMap[location[0] + dy[index]][location[1] + dx[index]] == -1:
                    # 큐에 없고
                    # --> not in 연산 시간이 오래 걸려서 시간 초과
                    # if [location[0] + dy[index], location[1] + dx[index]] not in queue:
                        # 이동 횟수로 바꿔주고 -> 이동 횟수가 아닌 바로 전꺼를 더해주자!
                        gamMap[location[0] + dy[index]][location[1] + dx[index]] = gamMap[location[0]][location[1]] + 1
                        # 큐에 추가 해줍니다.
                        queue.append([location[0] + dy[index], location[1] + dx[index]])
        # print(queue)

    # print(*gamMap)
    print(gamMap[y[0]][y[1]])


if __name__ == '__main__':

    n = int(input())
    array = []

    for _ in range(n):
        l = int(input())

        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        array.append([l, x, y])

        pass
    for i in array:
        solution(i[0], i[1], i[2])
