# https://www.acmicpc.net/problem/2447
# 별찍기


# ------------------------------------------------

# # 배열
# arrays = [['*']*3 for _ in range(3)]
#
#
# def solution(n):
#     if n == len(arrays):
#         return
#     if n % 3 == 1:
#         arrays[n][n] = ' '
#
#     solution(n+1)
#
#
# if __name__ == '__main__':
#     solution(0)
#
#
#

#
# n = int(input())
#
# data = [['*'] * n for _ in range(n)]
#
#
# def remove_stars(length, x, y):
#     global data
#     if length == 1:
#         return
#
#     # 지워 주는 부분
#     for row in data[x - length + length // 3: x - length // 3]:
#
#         row[y - length + length // 3:y - length // 3] = ' ' * (length // 3)
#
#
#     #  3 으로 나눠서 들어가는 부툰
#     for i in range(length // (length // 3)):
#         for j in range(length // (length // 3)):
#             remove_stars(length // 3, x - i * length // 3, y - j * length // 3)
#
#
# remove_stars(n, n, n)
# for row in data:
#     print(*row)
#
# -----------------------------------------------

# 일단 될때까지 다 옮기고
# 다시 옭기고
# 옮기면서 출력
# 하나 밑에서 옮기고
# 하나 남을걸 목적 지에 옮긴다
# 옮기면서 출력


# def solution(k):
#
#     for number in range(1, 10):
#         if number == 5:
#             print(' ', end='')
#             continue
#         print('*', end='')
#
#         if number % 3 == 0:
#             print()
#     return k
#
#

def printStar(k):
    printdata = [['-'] * k for _ in range(k)]
    for row in range(k):
        # if
        for col in range(k):
                printdata[row][col] = '*'

    return printdata


if __name__ == '__main__':

    k = 3

    for star in printStar(k):
        print(*star)
