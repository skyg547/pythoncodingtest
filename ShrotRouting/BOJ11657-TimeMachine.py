# https://www.acmicpc.net/problem/11657
# 타임머신

import sys

input = sys.stdin.readline


def solution(city, costList):
    # 2 차원 그래프별 초기화 0 번인덱스 제거
    ansewerCost = [[1e9] * (city + 1) for _ in range(city + 1)]

    # 간선의 값으로 초기화
    for cost in costList:
        ansewerCost[cost[0]][cost[1]] = cost[2]

    # 각 도시를 돌면서 최소 비용을로 초기화
    for middleCity in range(1, city + 1):  # 중간지점
        for cityStart in range(1, city + 1):  # 출발 지점
            for cityFinish in range(1, city + 1):  # 도착지점

                # 자기 도시는 = 0
                if cityStart == cityFinish:
                    ansewerCost[cityStart][cityFinish] = 0
                    continue
                ansewerCost[cityStart][cityFinish] = min(ansewerCost[cityStart][cityFinish],
                                                         ansewerCost[cityStart][middleCity] + ansewerCost[middleCity][
                                                             cityFinish])

        # 각 도시를 돌면서 최소 비용을로 초기화
    for middleCity in range(1, city + 1):  # 중간지점
        for cityStart in range(1, city + 1):  # 출발 지점
            for cityFinish in range(1, city + 1):  # 도착지점

                # 만약 한번더 돌아서 값이 변하면 음수로 되는 값이 있기 때문에 - 사이클이 있는거잇이라 무한 타임머신이 가능한다
                if (ansewerCost[cityStart][cityFinish] >
                        ansewerCost[cityStart][middleCity] + ansewerCost[middleCity][
                            cityFinish]):
                    ansewerCost[cityStart][cityFinish] = -1
                    print(-1)
                    exit()

    return ansewerCost[1:][0]


if __name__ == '__main__':
    n, m = 3, 4
    l = [[1, 2, 4],
         [1, 3, 3],
         [2, 3, - 1],
         [3, 1, - 2]]

    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]

    ans = (solution(n, l))

    for index in range(2, len(ans)):
        if ans[index] == 1e9:
            print(-1)
            continue

        print(ans[index])
