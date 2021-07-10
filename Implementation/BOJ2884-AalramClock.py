# https://www.acmicpc.net/problem/2884
# 알람시계


def solution(h, m):
    answer = []
    # 시간에서 45 분 적으면
    if m - 45 > 0:
        answer.append(h)
        answer.append(m - 45)
    else:
        if h - 1 < 0:
            answer.append(23)
            answer.append(60 - (45-m))
        else:
            answer.append(h-1)
            answer.append(60-(45-m))

    return answer


if __name__ == '__main__':
    h, m = map(int, input().split())

    print(*solution(h, m))
