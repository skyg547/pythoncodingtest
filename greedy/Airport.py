# # 공함
# # 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# # 1 초	256 MB	7657	2847	2083	38.053%
# # 문제
# # 오늘은 신승원의 생일이다.
# #
# # 박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.
# #
# # 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.
# #
# # 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.
# #
# # 신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?
# #
# # 입력
# # 첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
# #
# # 두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
# #
# # 이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.
# #
# # 출력
# # 승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.
# #
# # 예제 입력 1
# # 4
# # 3
# # 4
# # 1
# # 1
# # 예제 출력 1
# # 2
# # 예제 입력 2
# # 4
# # 6
# # 2
# # 2
# # 3
# # 3
# # 4
# # 4
# # 예제 출력 2
# # 3
#  테케는 맞았지만 힙으로 푸러야함

# def solution(G, g):
#     ans = 0
#     Gate = [0] * G
#     # print(Gate)
#     g.sort(reverse=True)
#
#     for plane in g:
#         # print(plane)
#         for gatenum in range(len(Gate), 0, -1):
#             # print(gatenum)
#             if gatenum <= plane:
#                 if Gate[gatenum-1] == 0:
#                     Gate[gatenum-1] = 1
#                     break
#         # print(Gate)
#
#     # print(Gate)
#     return sum(Gate)
#
#
# if __name__ == '__main__':
#     # G개의 게이트
#     # 각가 1에서 G까지 번호
#     # P개의 비행기 -> 순서대로
#     # i번째 비행기를 1번부터 G 게이트중 하나 도킹
#     # 도킹 못하면 -> 폐쇄 , 도착 X
#     # 최대 도킹 갯수
#
#     # 입력 G 게이트수 10**5
#     G = 4
#     G = int(input())
#     # 비행기수 10**5
#     P = 3
#     P = int(input())
#     # 가능한 게이트 넘버수
#     g = [4, 1, 1]
#     g = [int(input()) for _ in range(G)]
#
#     print(solution(G, g))
import sys

input = sys.stdin.readline


def parent_find(x):
    # 최대값 도킹 시키기
    if x == parent[x]:
        return x
    #  낮은값 도킹 찾기
    p = parent_find(parent[x])
    # 부모배열 바꿔주고 반환// 경로 압축
    parent[x] = p
    return parent[x]

# 부모 바꿔 주기
def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


def solution(g, plane):
    # 전역으로 부모 배열을 초기화
    global parent
    parent = [i for i in range(g + 1)]
    print(parent)
    # 최대 갯수 카운트
    cnt = 0

    for i in plane:
        #i의 부모 찾기,
        x = parent_find(i)
        # 0일때 도킹할수 없음
        if x == 0:
            break
        # 도킹후 번호 내려주기
        union(x, x - 1)
        # 최대갯수 추가
        cnt += 1
        print(i,parent)

    return cnt


if __name__ == '__main__':
    g = int(input())
    p = int(input())

    plane = [int(input()) for _ in range(p)]

    print(solution(g, plane))
