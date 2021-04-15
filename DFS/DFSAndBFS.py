# DFS and BFS
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	127620	45431	26126	33.791%
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque


def bfs(V, L, visited):
    queue = deque()
    queue.append(V)

    while queue:
        # 큐에서 빼서
        TempV = queue.popleft()
        # 방문처리 하고
        visited[TempV] = 1
        # 출력
        print(TempV, end=' ')

        # 간선 리스트 순회
        for i in L:
            # 정점이 지금 정점이고
            if i[0] == TempV:
                # 방문하지않고, 큐에 없으면
                if visited[i[1]] == 0 and i[1] not in queue:
                    # 큐애 추가
                    queue.append(i[1])

            # 정점이 지금 정점이고
            if i[1] == TempV:
                # 방문하지않고, 큐에 없으면
                if visited[i[0]] == 0 and i[0] not in queue:
                    # 큐애 추가
                    queue.append(i[0])


def dfs(V, L, visited):
    ans = []

    # 방문 처리
    visited[V] = 1
    # 방문한거 출력
    print(V, end=' ')

    # 그래프를 도는데
    for i in L:
        # 만약 방문 처리 가 되지않았다면
        if visited[i[1]] == 0 and i[0] == V:
            dfs(i[1], L, visited)
        if visited[i[0]] == 0 and i[1] == V:
            dfs(i[0], L, visited)

# 12 % 탈락
def solution(N, V, L):
    # 인덱스를 편하게 관리하고자 n+1 곱해줌
    visited = [0] * (N + 1)

    dfs(V, L, visited)

    #한칸 뛰우기
    print()
    # 초기화
    visited = [0] * (N + 1)
    bfs(V, L, visited)


if __name__ == '__main__':
    N, M, V = 4, 5, 1
    L = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 4],
        [3, 4]
    ]
    N, M, V = map(int, input().split())

    # 12 % 탈락반례
    # 3 2 1
    # 1 3
    # 2 1
    # 3 2 1
    # 1 2
    # 1 3
    # 이유 :

    # 해결법 -> 솔트
    L = [sorted(list(map(int, input().split()))) for _ in range(M)]
    L.sort(key=lambda x: (x[0], x[1]))
    solution(N, V, L)
