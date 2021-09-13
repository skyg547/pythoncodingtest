# https://www.acmicpc.net/problem/1085
# 직사각형에서 탈출
# 0.0 랑 가까운지도 생각 하자

def solution():
    return


if __name__ == '__main__':
    x, y, w, h = map(int, input().split())

    print(min(w - x, h - y,
              x - 0, y - 0))
