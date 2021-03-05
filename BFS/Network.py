# 네트워크
# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.
# 입출력 예
# n	computers	return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
from collections import deque

def solution(n, computers):
    answer = 0
    visted = [False]*n
    queue = deque([0])

    graph = []
    for i in range(n):
        graph.append([])



    for i in range(n):
        for j in range(i,n):
            if i==j:
                pass
            else:
                if computers[i][j] == 1:
                    graph[i].append(j)

    print(graph)
    # #첫번째 방문 처리
    # visted[0] = True
    #
    # while queue:
    #
    #     v = queue.popleft()
    #     for i in computers[v]:
    #         if not visted[i]:
    #             queue.append(i)
    #             #연결된곳 방문 처리
    #             visted[i] = True

    for j in range(len(visted)):
        while not visted[j]:
            visted[j] = True
            answer += 1
            while queue:

                v = queue.popleft()
                for i in computers[v]:
                    if not visted[i]:
                        queue.append(i)
                        # 연결된곳 방문 처리
                        visted[i] = True




    return answer

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)
n = 3
c = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, c))
