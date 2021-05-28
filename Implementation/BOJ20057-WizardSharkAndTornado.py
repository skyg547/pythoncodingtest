# https://www.acmicpc.net/problem/20057
# ㅁㅏ 법사 상어와 토네이도
#
# 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양
# 격자의 가운데 칸부터 토네이도의 이동이 시작
# x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸
# 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼
#  소수점 아래는 버린다
# . α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다
# 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.
# 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전
# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다.
#  모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양


sumAns = 0


# 왼쪽
def left(l, x, y):
    global sumAns

    # 바로 위 1%
    if 0 <= x - 1 < len(l) and 0 <= y < len(l):
        l[x - 1][y] += (l[x][y - 1] // 100)
    else:
        sumAns += (l[x][y - 1] // 100)

    # 바로 아래 1%
    if 0 <= x + 1 < len(l) and 0 <= y < len(l):
        l[x + 1][y] += (l[x][y - 1] // 100)
    else:
        sumAns += (l[x][y - 1] // 100)

    # 바로 위 대각선 7%
    if 0 <= x - 1 < len(l) and 0 <= y - 1 < len(l):
        l[x - 1][y - 1] += (l[x][y - 1] // 100) * 7
    else:
        sumAns += (l[x][y - 1] // 100) * 7

    # 바로 아래 대각선 7%
    if 0 <= x + 1 < len(l) and 0 <= y - 1 < len(l):
        l[x + 1][y - 1] += (l[x][y - 1] // 100) * 7
    else:
        sumAns += (l[x][y - 1] // 100) * 7

    # 바로 2번째위 대각선 2%
    if 0 <= x - 2 < len(l) and 0 <= y - 1 < len(l):
        l[x - 2][y - 1] += (l[x][y - 1] // 100) * 2
    else:
        sumAns += (l[x][y - 1] // 100) * 2

    # 바로 2번아래 대각선 2%
    if 0 <= x + 2 < len(l) and 0 <= y - 1 < len(l):
        l[x + 2][y - 1] += (l[x][y - 1] // 100) * 2
    else:
        sumAns += (l[x][y - 1] // 100) * 2

    # 바로 위 번째 왼쪽 대각선 10%
    if 0 <= x - 1 < len(l) and 0 <= y - 2 < len(l):
        l[x - 1][y - 2] += (l[x][y - 1] // 100) * 10
    else:
        sumAns += (l[x][y - 1] // 100) * 10

    # 바로 아래 번째 왼쪽 대각선 10%
    if 0 <= x + 1 < len(l) and 0 <= y - 2 < len(l):
        l[x + 1][y - 2] += (l[x][y - 1] // 100) * 10
    else:
        sumAns += (l[x][y - 1] // 100) * 10

    # 같은 라인 왼쪽 3번째 5%
    if 0 <= x < len(l) and 0 <= y - 3 < len(l):
        l[x][y - 3] += (l[x][y - 1] // 100) * 5
    else:
        sumAns += (l[x][y - 1] // 100) * 5

    # a에 남는 거
    if 0 <= x < len(l) and 0 <= y - 2 < len(l):
        l[x][y - 2] += (l[x][y - 1] // 100) * 55
    else:
        sumAns += (l[x][y - 1] // 100) * 55


# 오른쪽으로 휘날리는거
def right(l, x, y):
    global sumAns

    # 바로 위 1%
    if 0 <= x - 1 < len(l) and 0 <= y < len(l):
        l[x - 1][y] += (l[x][y + 1] // 100)
    else:
        sumAns += (l[x][y + 1] // 100)

    # 바로 아래 1%
    if 0 <= x + 1 < len(l) and 0 <= y < len(l):
        l[x + 1][y] += (l[x][y + 1] // 100)
    else:
        sumAns += (l[x][y + 1] // 100)

    # 바로 위 대각선 7%
    if 0 <= x - 1 < len(l) and 0 <= y + 1 < len(l):
        l[x - 1][y + 1] += (l[x][y + 1] // 100) * 7
    else:
        sumAns += (l[x][y + 1] // 100) * 7

    # 바로 아래 대각선 7%
    if 0 <= x + 1 < len(l) and 0 <= y + 1 < len(l):
        l[x + 1][y + 1] += (l[x][y + 1] // 100) * 7
    else:
        sumAns += (l[x][y + 1] // 100) * 7

    # 바로 2번째위 대각선 2%
    if 0 <= x - 2 < len(l) and 0 <= y + 1 < len(l):
        l[x - 2][y + 1] += (l[x][y + 1] // 100) * 2
    else:
        sumAns += (l[x][y + +1] // 100) * 2

    # 바로 2번아래 대각선 2%
    if 0 <= x + 2 < len(l) and 0 <= y + 1 < len(l):
        l[x + 2][y + 1] += (l[x][y + 1] // 100) * 2
    else:
        sumAns += (l[x][y + 1] // 100) * 2

    # 바로 위 번째 왼쪽 대각선 10%
    if 0 <= x - 1 < len(l) and 0 <= y + 2 < len(l):
        l[x - 1][y + 2] += (l[x][y + 1] // 100) * 10
    else:
        sumAns += (l[x][y + 1] // 100) * 10

    # 바로 아래 번째 왼쪽 대각선 10%
    if 0 <= x + 1 < len(l) and 0 <= y + 2 < len(l):
        l[x + 1][y + 2] += (l[x][y + 1] // 100) * 10
    else:
        sumAns += (l[x][y + 1] // 100) * 10

    # 같은 라인 왼쪽 3번째 5%
    if 0 <= x < len(l) and 0 <= y + 3 < len(l):
        l[x][y + 3] += (l[x][y + 1] // 100) * 5
    else:
        sumAns += (l[x][y + 1] // 100) * 5

    # a에 남는 거
    if 0 <= x < len(l) and 0 <= y + 2 < len(l):
        l[x][y + 2] += (l[x][y + 1] // 100) * 55
    else:
        sumAns += (l[x][y + 1] // 100) * 55


# 위
def up(l, x, y):
    global sumAns

    # 바로 왼쪽 1%
    if 0 <= x < len(l) and 0 <= y - 1 < len(l):
        l[x][y - 1] += (l[x - 1][y] // 100)
    else:
        sumAns += (l[x - 1][y] // 100)

    # 바로 오른쪽 1%
    if 0 <= x < len(l) and 0 <= y + 1 < len(l):
        l[x][y + 1] += (l[x - 1][y] // 100)
    else:
        sumAns += (l[x - 1][y] // 100)

    # 바로 위 대각선 7%
    if 0 <= x - 1 < len(l) and 0 <= y - 1 < len(l):
        l[x - 1][y - 1] += (l[x - 1][y] // 100) * 7
    else:
        sumAns += (l[x - 1][y] // 100) * 7

    # 바로 아래 대각선 7%
    if 0 <= x - 1 < len(l) and 0 <= y + 1 < len(l):
        l[x - 1][y + 1] += (l[x - 1][y] // 100) * 7
    else:
        sumAns += (l[x - 1][y] // 100) * 7

    # 바로 2번째위 대각선 2%
    if 0 <= x - 1 < len(l) and 0 <= y - 2 < len(l):
        l[x - 1][y - 2] += (l[x - 1][y] // 100) * 2
    else:
        sumAns += (l[x - 1][y] // 100) * 2

    # 바로 2번아래 대각선 2%
    if 0 <= x - 1 < len(l) and 0 <= y + 2 < len(l):
        l[x - 1][y + 2] += (l[x - 1][y] // 100) * 2
    else:
        sumAns += (l[x - 1][y] // 100) * 2

    # 바로 위 번째 왼쪽 대각선 10%
    if 0 <= x - 2 < len(l) and 0 <= y - 1 < len(l):
        l[x - 2][y - 1] += (l[x - 1][y] // 100) * 10
    else:
        sumAns += (l[x - 1][y] // 100) * 10

    # 바로 아래 번째 왼쪽 대각선 10%
    if 0 <= x - 2 < len(l) and 0 <= y + 1 < len(l):
        l[x - 2][y + 1] += (l[x - 1][y] // 100) * 10
    else:
        sumAns += (l[x - 1][y] // 100) * 10

    # 같은 라인 왼쪽 3번째 5%
    if 0 <= x - 3 < len(l) and 0 <= y < len(l):
        l[x - 3][y] += (l[x - 1][y] // 100) * 5
    else:
        sumAns += (l[x - 1][y] // 100) * 5

    # a에 남는 거
    if 0 <= x - 2 < len(l) and 0 <= y < len(l):
        l[x - 2][y] += (l[x - 1][y] // 100) * 55
    else:
        sumAns += (l[x - 1][y] // 100) * 55


# 아래
def down(l, x, y):
    global sumAns

    # 바로 왼쪽 1%
    if 0 <= x < len(l) and 0 <= y - 1 < len(l):
        l[x][y - 1] += (l[x + 1][y] // 100)
    else:
        sumAns += (l[x + 1][y] // 100)

    # 바로 오른쪽 1%
    if 0 <= x < len(l) and 0 <= y + 1 < len(l):
        l[x][y + 1] += (l[x + 1][y] // 100)
    else:
        sumAns += (l[x + 1][y] // 100)

    # 바로 위 대각선 7%
    if 0 <= x + 1 < len(l) and 0 <= y - 1 < len(l):
        l[x + 1][y - 1] += (l[x + 1][y] // 100) * 7
    else:
        sumAns += (l[x + 1][y] // 100) * 7

    # 바로 아래 대각선 7%
    if 0 <= x + 1 < len(l) and 0 <= y + 1 < len(l):
        l[x + 1][y + 1] += (l[x + 1][y] // 100) * 7
    else:
        sumAns += (l[x + 1][y] // 100) * 7

    # 바로 2번째위 대각선 2%
    if 0 <= x + 1 < len(l) and 0 <= y - 2 < len(l):
        l[x + 1][y - 2] += (l[x + 1][y] // 100) * 2
    else:
        sumAns += (l[x + 1][y] // 100) * 2

    # 바로 2번아래 대각선 2%
    if 0 <= x + 1 < len(l) and 0 <= y + 2 < len(l):
        l[x + 1][y + 2] += (l[x + 1][y] // 100) * 2
    else:
        sumAns += (l[x + 1][y] // 100) * 2

    # 바로 위 번째 왼쪽 대각선 10%
    if 0 <= x + 2 < len(l) and 0 <= y - 1 < len(l):
        l[x + 2][y - 1] += (l[x + 1][y] // 100) * 10
    else:
        sumAns += (l[x + 1][y] // 100) * 10

    # 바로 아래 번째 왼쪽 대각선 10%
    if 0 <= x + 2 < len(l) and 0 <= y + 1 < len(l):
        l[x + 2][y + 1] += (l[x + 1][y] // 100) * 10
    else:
        sumAns += (l[x + 1][y] // 100) * 10

    # 같은 라인 왼쪽 3번째 5%
    if 0 <= x + 3 < len(l) and 0 <= y < len(l):
        l[x + 3][y] += (l[x + 1][y] // 100) * 5
    else:
        sumAns += (l[x + 1][y] // 100) * 5

    # a에 남는 거
    if 0 <= x + 2 < len(l) and 0 <= y < len(l):
        l[x + 2][y] += (l[x + 1][y] // 100) * 55
    else:
        sumAns += (l[x + 1][y] // 100) * 55


def solution(l):
    cnt = 1
    direction = 0
    x = len(l) // 2
    y = len(l) // 2
    while 1:
        # 도는 횟수

        # 마지막 도는것

        if cnt == len(l) - 1:
            for _ in range(3):
                # 왼쪽방향
                if direction == 0:
                    for _ in range(cnt):
                        left(l, x, y)
                        y -= 1

                # 아래 방향
                elif direction == 1:
                    for _ in range(cnt):
                        down(l, x, y)
                        x += 1

                # 오른쪽 방향
                elif direction == 2:
                    for _ in range(cnt):
                        right(l, x, y)
                        y += 1

                # 위 방향
                elif direction == 3:
                    for _ in range(cnt):
                        up(l, x, y)
                        x -= 1

                # 횟수가 끝날때 마다 방향이 바뀌고
                direction = (direction + 1) % 4
            # 반복문 종료 리턴
            break

        else:
            # 2번은 반복하고
            for _ in range(2):

                # 왼쪽방향
                if direction == 0:
                    for _ in range(cnt):
                        left(l, x, y)
                        y -= 1

                # 아래 방향
                elif direction == 1:
                    for _ in range(cnt):
                        down(l, x, y)
                        x += 1

                # 오른쪽 방향
                elif direction == 2:
                    for _ in range(cnt):
                        right(l, x, y)
                        y += 1

                # 위 방향
                elif direction == 3:
                    for _ in range(cnt):
                        up(l, x, y)
                        x -= 1

                # 횟수가 끝날때 마다 방향이 바뀌고
                direction = (direction + 1) % 4

        # 그리고 횟수가 올라가고
        cnt += 1

    return sumAns


if __name__ == '__main__':
    n = 7
    l = [[1, 2, 3, 4, 5, 6, 7],
         [1, 2, 3, 4, 5, 6, 7],
         [1, 2, 3, 4, 5, 6, 7],
         [1, 2, 3, 0, 5, 6, 7],
         [1, 2, 3, 4, 5, 6, 7],
         [1, 2, 3, 4, 5, 6, 7],
         [1, 2, 3, 4, 5, 6, 7]]
    print(solution(l))
