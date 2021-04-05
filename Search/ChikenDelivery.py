# 치킨 배달 분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	512 MB	33896	15780	8962	42.388%
# 문제
# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
#
# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
#
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
#
# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.
#
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2
# 0은 빈 칸, 1은 집, 2는 치킨집이다.
#
# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.
#
# (5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.
#
# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.
#
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
#
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
#
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
#
# 출력
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

from itertools import combinations


def solution(s, lists):
    chikenLocation = []
    answerlist = []
    # 모든 2 좌표를 가져온다

    for i in lists:
        # 행에 j가 중복 될경우 맨 처음거만 나옴 index 함수가
        for j in range(len(i)):
            tempLocation = []
            if i[j] == 2:
                #  행
                tempLocation.append(lists.index(i))
                # 열
                tempLocation.append(j)
            # 비어있지 않으면 치킨 좌표배열에 추가
            if tempLocation:
                chikenLocation.append(tempLocation)
    # 2좌표를 배열로 만든다

    # s개 씩 조합 을 짜보고 ,
    combilist = list(combinations(chikenLocation, s))
    # print(combilist)

    # 배열 인덱스에 x,y 좌표를 다 받아오고 m개 조합을 돌린다,

    # 배열의 횟수만큼 반복한다
    for i in combilist:
        copylists = lists.copy()
        # 리스트에 모든 2를 0으로 바꿔 준다
        for j in copylists:
            for k in j:
                if k == 2:
                    copylists[copylists.index(j)][j.index(k)] = 0
        # 조합배열을 돌아가면서 에 있는 좌표를 2로 바꿔준다
        for j in i:
            copylists[j[0]][j[1]] = 2

        # 도시의 치킨 거리
        sumlist = []
        for j in copylists:
            for k in range(len(j)):
                if j[k] == 1:

                    # 치킨거리는 치킨 집에서 가장 작은게 치킨거리이다
                    mins = 1e9
                    for x in i:

                        # | r1 - r2 | + | c1 - c2 |
                        # 행 + 열
                        if mins > abs(x[0] - copylists.index(j)) + abs(x[1] - k):
                            mins = abs(x[0] - copylists.index(j)) + abs(x[1] - k)
                    # 이게 도시의 치킨 거리다

                    sumlist.append(mins)

        # 모든 치킨거리를 이거를 다 합쳐준다
        # 배열에 담아준다
        answerlist.append(sum(sumlist))


    # 최소값을 찾아서 출력한다
    return min(answerlist)


# 1 = 집
# 2 = 집치킨

n, s = 5, 2
lists = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2],
]

#입력
n, s = map(int,input().split())
lists = []
for i in range(n):
    lists.append(list(map(int, input().split())))
# print(lists, n, s)

#출력
print(solution(s, lists))
