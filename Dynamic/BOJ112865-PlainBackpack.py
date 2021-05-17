# 평범한 배낭
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	32208	12258	8082	36.442%
# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.
#
# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
#
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
#
# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
#
# 입력으로 주어지는 모든 수는 정수이다.
#
# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
#
# 예제 입력 1
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 예제 출력 1
# 14

# 냅색 쪼깰수 업는 문제
def solution(k, l):
    # 물건에 따라 비용에 담을 무게 배열을 생성해준다.
    priceList = [[0 for _ in range(k + 1)] for _ in range(len(l))]

    # 물건 별로 돌면서
    for y in range(1, len(l)):
        # 무게 별로 돌고
        for x in range(1, k + 1):
            # 무게를 담아주고
            weight = l[y][0]
            # 물건을 담아주고
            value = l[y][1]

            # 무게가 현재 담을 무게 보다 작다면 ? -> 담을수 있다면

            if x < weight: # 위에 값을 그냥 담아준다
                priceList[y][x] = priceList[y - 1][x]
            else:
                # 아니면 둘중 큰거를 골라준다,
                priceList[y][x] = max(value + priceList[y - 1][x - weight], priceList[y - 1][x])

    # for element in l:
    #     priceList.append((element[1] / element[0], element[0]))

    # print(priceList)

    return priceList[len(l) - 1][k]


if __name__ == '__main__':
    N, K = 4, 7
    L = [[0, 0],
         [6, 13],
         [4, 8],
         [3, 6],
         [5, 12]
         ]

    N, K = map(int, input().split())

    L = []

    L.append([0, 0])
    for _ in range(N):
        L.append(list(map(int, input().split())))
    print(solution(K, L))
