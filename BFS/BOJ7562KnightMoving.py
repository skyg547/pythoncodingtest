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
# dx = [-2, -1, 1, 2, -2, -1, 1, 2]
# dy = [-1, -2, -2, -1, 1, 2, 2, 1]
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

def solution(l,x,y):

    # 일단 bfs 로 돌면서 각 최소값들을 체크해서 판을 모두 채우자

    # 그러면 방문한 곳은 0 이 아닌 만들어 주자

    # 일단 판을 만들고
    gamMap = [[-1]*l for i in range(l)]

    # for index in gamMap:
    #     for element in range(l):
    #         index.append(-1)

    # 게임 맵이 -1 이 아니면
    for y in range(l):
        for x in

        queue if
            queue = deque()

        # bfs 수행


    return



if __name__ == '__main__':

    n = 3

    l = 8
    x = [0, 0]

    y = [7, 0]

    print(solution(l, x, y))

