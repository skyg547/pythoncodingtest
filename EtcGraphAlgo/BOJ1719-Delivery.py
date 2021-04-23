# 택배
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	2186	1192	762	56.908%
# 문제
# 명우기업은 2008년부터 택배 사업을 새로이 시작하기로 하였다. 우선 택배 화물을 모아서 처리하는 집하장을 몇 개 마련했지만, 택배 화물이 각 집하장들 사이를 오갈 때 어떤 경로를 거쳐야 하는지 결정하지 못했다. 어떤 경로를 거칠지 정해서, 이를 경로표로 정리하는 것이 여러분이 할 일이다.
#
#
#
# 예시된 그래프에서 굵게 표시된 1, 2, 3, 4, 5, 6은 집하장을 나타낸다. 정점간의 간선은 두 집하장간에 화물 이동이 가능함을 나타내며, 가중치는 이동에 걸리는 시간이다. 이로부터 얻어내야 하는 경로표는 다음과 같다.
#
#
#
# 경로표는 한 집하장에서 다른 집하장으로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것이다. 예를 들어 4행 5열의 6은 4번 집하장에서 5번 집하장으로 최단 경로를 통해 가기 위해서는 제일 먼저 6번 집하장으로 이동해야 한다는 의미이다.
#
# 이와 같은 경로표를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 두 수 n과 m이 빈 칸을 사이에 두고 순서대로 주어진다. n은 집하장의 개수로 200이하의 자연수, m은 집하장간 경로의 개수로 10000이하의 자연수이다. 이어서 한 줄에 하나씩 집하장간 경로가 주어지는데, 두 집하장의 번호와 그 사이를 오가는데 필요한 시간이 순서대로 주어진다. 집하장의 번호들과 경로의 소요시간은 모두 1000이하의 자연수이다.
#
# 출력
# 예시된 것과 같은 형식의 경로표를 출력한다.
#
# 예제 입력 1
# 6 10
# 1 2 2
# 1 3 1
# 2 4 5
# 2 5 3
# 2 6 7
# 3 4 4
# 3 5 6
# 3 6 7
# 4 6 4
# 5 6 2
# 예제 출력 1
# - 2 3 3 2 2
# 1 - 1 4 5 5
# 1 1 - 4 5 6
# 3 2 3 - 6 6
# 2 2 3 6 - 6
# 5 5 3 4 5 -
from collections import deque


# 다익스트라로 구현하고자 했으나 실패..
# # 최소 신장 트리?
# def solution(n, timetable):
#     # 최소값 경로를 저장 할 테이블 만들기 저장할 테이블 만들기
#     answer = [[]]
#
#     # 경로 테이블을 만들기
#     routetable = [['-' for _ in range(n + 1)] for _ in range(n + 1)]
#     for route in timetable:
#         routetable[route[0]][route[1]] = route[2]
#
#     for indexY in range(1, len(routetable)):
#         # 결과값 담을 테이블
#         dp = [1001] * (n + 1)
#         # 방문을 체크해줄 필수
#         visited = [False] * (n + 1)
#         visited[0] = True
#         # 탐색을 할 큐
#         queue = deque()
#         for indexX in range(1, len(routetable)):
#
#             if routetable[indexY][indexX] != '-':
#                 dp[indexX] = routetable[indexY][indexX]
#                 visited[indexX] = True
#
#         # 방문하지 않는 배열이 있다면 체크
#         while not all(visited):
#
#
#         # 1일때 2 ,3 하고
#         # 그리고 2, 3 bfs
#         # 근데 만약 크다? 그럼 바로 내팽겨 치기
#         # 그리고 방문 했던 곳이다? 그럼 방문 하지마
#         answer.append(dp)
#     print(answer)


def solution(n, timetable):
    # 최소값 경로 저장할 테이블 만들기
    answer = [["-" for _ in range(n + 1)] for _ in range(n + 1)]
    # 경로 테이블을 만들기
    routetable = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0 으로 초기화
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if y == x:
                routetable[y][x] = 0


    for route in timetable:
        # 그래프의 가중치 값 추가
        routetable[route[0]][route[1]] = route[2]
        # 반대 것도 해줘야함
        routetable[route[1]][route[0]] = route[2]

        # 정답 배열에 맨 처음 최단거리  가는거 추가
        answer[route[0]][route[1]] = route[1]
        # 반대 노드도 해줘야 한다
        answer[route[1]][route[0]] = route[0]

    # 플로이드 워셜 알고리즘
    for tempnode in range(1, n + 1):  # 거쳐가는 노드
        for startnode in range(1, n + 1):  # 시작 노드
            for endnode in range(1, n + 1):  # 끝나는 노드
                if routetable[startnode][endnode] > routetable[startnode][tempnode] + routetable[tempnode][endnode]:
                    # 비용을 최단 거리로 갱신
                    routetable[startnode][endnode] = routetable[startnode][tempnode] + routetable[tempnode][endnode]
                    # 먼저 들러야하는 지점인 (a, k)의 집하장 값으로 갱신
                    answer[startnode][endnode] = answer[startnode][tempnode]

    # 맨 처음 것 제거
    for arrays in answer:
        arrays.remove('-')

    return answer


if __name__ == '__main__':
    n, m = 6, 10
    # 노드 1 , 노드 2 , 시간

    timetable = [
        [1, 2, 2],
        [1, 3, 1],
        [2, 4, 5],
        [2, 5, 3],
        [2, 6, 7],
        [3, 4, 4],
        [3, 5, 6],
        [3, 6, 7],
        [4, 6, 4],
        [5, 6, 2]
    ]
    #
    n, m = map(int , input().split())

    timetable = [list(map(int, input().split()))for _ in range(m)]

    answer = solution(n, timetable)
    for index in range(1,len(answer)):
        print(*answer[index])