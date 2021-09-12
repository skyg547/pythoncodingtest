# https://www.acmicpc.net/problem/1085
# 직사각형에서 탈출


def solution():
    return


if __name__ == '__main__':
    x, y, w, h = map(int,input().split())

    print(min(w-x, h-y))
