# 문제
#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+
# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
#
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
#
# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
#
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.
from itertools import combinations, product


def solution(n, dice):
    ans = 0
    # 어떠헤해야 최소가 나올까?

    # 1 일때 예외처리
    if n == 1:
        return sum(dice)-max(dice)
    # 최소를 구하는 방법
    a = [dice[0], dice[5]]
    b = [dice[2], dice[3]]
    c = [dice[1], dice[4]]
    min1 = min(dice)

    # 카타전 프로덕트를 이용해 2개씩 뽑아서 최소 값을 저장
    templist = set(list(product(*[b + c, a])) +
                   list(product(*[b, a + c])) +
                   list(product(*[c, a + b])))

    min2 = min(list(map(lambda x: sum(x), templist)))

    # 카티전 프로덕트를 이용해 3개의 리스트에서 3개씩 뽑아서 조합 하고 최소값 저장

    templist = [a, b, c]
    # print(*templist)
    # print(templist)
    # print(list(product(*['abc', 'ab'])))

    templist = set(list(product(*templist)))  # 곱하기를 잘 모르겠습

    min3 = min(list(map(lambda x: sum(x), templist)))

    # 최소 3개면 4개는 고정 큐브 천장 4개
    ans += min3 * 4
    # 최소 2개면 4개 고정 큐브 바닥 4개
    ans += min2 * 4
    #  min 2개 짜리 8개 n -2 개 큐브 사이드 8개
    ans += min2 * (n - 2) * 8
    #  min 1개 짜리 5개 (n-2)**2 큐브 중앙 5개
    ans += min1 * 5 * ((n - 2) ** 2)
    # min 1개 짜리 (n-2) 4게 큐브 바닥중앙 4개
    ans += min1 * (n - 2) * 4
    return ans


if __name__ == '__main__':
    n = 3
    dice = [1,
            2,
            3,
            4,
            5,
            6]

    n = int(input())
    dice = list(map(int, input().split()))
    print(solution(n, dice))
