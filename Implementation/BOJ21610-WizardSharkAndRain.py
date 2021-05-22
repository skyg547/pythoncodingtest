# https://www.acmicpc.net/problem/21610
# 마법사 상어와 비바라기


#  N×N인 격자에서 연습 o
# 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지 o
# 바구니에 저장할 수 있는 물의 양에는 제한이 없다.o
# (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양o
# 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N) o
# 법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열 o
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지 o
# 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행
# o
# 모든 구름이 di 방향으로 si칸 이동한다. o
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다. o
# 구름이 모두 사라진다. o

# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. o
# 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다. o

# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.o

# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다. o

# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다. ㅇ
#
# 물의 양의 합

import sys

input = sys.stdin.readline

# 방향 좌표 구현
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

# 대각선 사방 탐색
dy2 = [1, -1, 1, -1]
dx2 = [1, -1, -1, 1]


# 구름 이동 함수
def move(l, moving, cloud):
    # 지정된 횟수를 반복해주면서
    for i in range(moving[1]):
        # 모든 구름들에게 방향 이동해준다
        for cloudMove in cloud:
            # 각 칸의 넘어가면 그 다음 칸으로 넘어가게 설정
            cloudMove[0] = (cloudMove[0] + dx[moving[0] - 1]) % (len(l))
            cloudMove[1] = (cloudMove[1] + dy[moving[0] - 1]) % (len(l))


# 비내리기
def rain(l, cloud):
    # 각 구름을 돌면서 비를 내려준다
    for clouds in cloud:
        # 비를 내려 1 씩 증가
        l[clouds[0]][clouds[1]] = l[clouds[0]][clouds[1]] + 1


# 물복사 버그
def bug(l, cloud):
    for clouds in cloud:
        # 대각선 사방 탐색
        for direction in range(4):
            # 사방 탐색 할때 경계 범위를 벗어나지 않으면
            if 0 <= clouds[0] + dx2[direction] <= len(l) - 1 and 0 <= clouds[1] + dy2[direction] <= len(l) - 1:
                # 그때 대각선에 물이 양이 있으면 !?
                if l[clouds[0] + dx2[direction]][clouds[1] + dy2[direction]] > 0:
                    # 구름 위치의 물양 증가
                    l[clouds[0]][clouds[1]] = l[clouds[0]][clouds[1]] + 1


# 새로운 구름 설정
def refresh(l, cloud, prevCloud):
    # 모든 바구니를 탐색 하는데
    for x in range(len(l)):
        for y in range(len(l)):
            # 지금 위치가 그전 구름 위치가 아니여야 하고
            if [x, y] not in prevCloud:
                # 물의 양이 2 이상이면
                if l[x][y] >= 2:
                    # 물의 양이 2 줄어 들고
                    l[x][y] -= 2
                    # 구름에 추가해준다
                    cloud.append([x, y])


def solution(l, o):
    # 처음 구름의 위치
    cloud = [[len(l) - 1, 0], [len(l) - 1, 1], [len(l) - 1 - 1, 0], [len(l) - 1 - 1, 1]]

    for moving in o:
        # 이동 함수 구현
        move(l, moving, cloud)
        # 비내리는 함수 구현
        rain(l, cloud)

        # 물복사 버그 함수 구현
        bug(l, cloud)

        # 이전 구름 저장
        preCloud = cloud
        # 구름 초기화
        cloud = []

        # 모든 칸 검사 및 새로움 구름 지정 구현
        refresh(l, cloud, preCloud)
    # 모든 칸 깍기 구현

    # 모든 물의양 합치기
    sum = 0
    for x in l:
        for y in x:
            sum += y
    return sum


if __name__ == '__main__':
    n, m = 5, 4
    l = [[0, 0, 1, 0, 2],
         [2, 3, 2, 1, 0],
         [4, 3, 2, 9, 0],
         [1, 0, 2, 9, 0],
         [8, 8, 2, 1, 0]]
    o = [[1, 3],
         [3, 4],
         [8, 1],
         [4, 8]]

    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    o = [list(map(int, input().split())) for _ in range(m)]
    print(solution(l, o))
