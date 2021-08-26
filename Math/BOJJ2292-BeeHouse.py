# https://www.acmicpc.net/problem/2292
# 벌집


def solution():
    return


if __name__ == '__main__':

    answer = int(input())

    number = 1
    cnt = 0;
    while (1):
        if (number >= answer):
            print(
                cnt + 1
            )
            break
        cnt += 1
        number += (cnt * 6)
