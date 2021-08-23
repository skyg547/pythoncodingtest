# https://www.acmicpc.net/problem/1712
# 손익 분기점


def solution():
    return


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    if c-b <= 0 :
        print(-1)
        exit()

    count = 1

    while (c-b) * count <= a :
        count += 1
    # count = 1
    # while a + (b * count) >= c * count:
    #     count += 1
    #     print(count)

    print(count)

