# 최단경로
# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
#
# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다.
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
#
# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
#
# 예제 입력 1
# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 예제 출력 1
# 0
# 2
# 3
# 7
# INF
import sys, _heapq


# 1차 시도 -> 메모리 초과
# 2차 시기
def solution(v, k, l):
    # 방문 배열 만들어주고
    # visted = [0] * (v + 1)
    # 출발 노드 방문 처리

    # 최솟값 배열
    minArray = [int(1e9)] * (v + 1)
    minArray[k] = 0

    # 경로값 만들어 주고
    # route = [[int(1e9) for _ in range(v + 1)] for _ in range(v + 1)]
    graph = [[] for _ in range(v + 1)]

    # 경로 바꿔 주기 -> 양쪽 모든 간선을 연결 해줘야 한다
    for element in l:
        # route[element[0]][element[1]] = element[2]
        # route[element[1]][element[0]] = element[2]
        graph[element[0]].append((element[1], element[2]))
        # graph[element[1]].append((element[0], element[2])) // 단방향 그래프 ?

        q = []
        # 최소힙 사용 시간복잡도 줄이기
        # 힙푸시를 이용하기 0 = k로 가는 최소값
        _heapq.heappush(q, (0, k))

        # 큐가 있을때
    while q:
        # dist = 비용 , now = 현재 노드
        # 최단거리의 노드 끄내기, heapop 은 가장 작은 값이 출력된다. 비용이
        dist, now = _heapq.heappop(q)
        # 방문된 노드라 라면 무시하기-> 이미 처리가 끝났슴
        # if visted[now] == 1:
        #     continue
        # 방문처리
        # visted[now] = 1

        # 지금 볼려는 곳이, 들어온 경로 보다 작으면 굳이 비교 할 필요가 없음,
        if minArray[now] < dist:
            continue

        # 현재 노드의 비용들을 돌아보면서
        for cost in graph[now]:
            # 새로운 비용은 현재 거리랑, 최소 경로를 더해 주는데
            newCost = dist + cost[1]
            # newCost = route[now][cost] + dist
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if newCost < minArray[cost[0]]:
                minArray[cost[0]] = newCost
                _heapq.heappush(q, (newCost, cost[0]))

    # print(l)
    # print(route)
    # print(minArray)

    return minArray


input = sys.stdin.readline

# 다익스트라
if __name__ == '__main__':
    v, e = 5, 6
    k = 1
    l = [
        [5, 1, 1],
        [1, 2, 2],
        [1, 3, 3],
        [2, 3, 4],
        [2, 4, 5],
        [3, 4, 6]]
    v, e = map(int, input().split())
    k = int(input())
    l = [list(map(int, input().split())) for _ in range(e)]

    answer = solution(v, k, l)
    for i in range(1, len(answer)):

        if answer[i] == 1e9:
            print("INF")
        else:
            print(answer[i])
