# https://www.acmicpc.net/problem/2447
# 별찍기

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

n = int(input())

data = [['*'] * n for _ in range(n)]


def remove_stars(length, x, y):
    global data
    if length == 1:
        return

    # 지워 주는 부분
    for row in data[x - length + length // 3: x - length // 3]:

        row[y - length + length // 3:y - length // 3] = ' ' * (length // 3)


    #  3 으로 나눠서 들어가는 부툰
    for i in range(length // (length // 3)):
        for j in range(length // (length // 3)):
            remove_stars(length // 3, x - i * length // 3, y - j * length // 3)


remove_stars(n, n, n)
for row in data:
    print(*row)
