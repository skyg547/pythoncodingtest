# 랭퍼든 수열쟁이야!! 출처분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	179	132	98	75.969%
# 문제
# 랭퍼드 수열은 다음 조건을 만족하는 길이 2n의 수열이다.
#
# 1 이상 n 이하의 자연수가 각각 두 개씩 들어 있다.
# 두 개의 1 사이에는 정확히 1개의 수가 있다.
# 두 개의 2 사이에는 정확히 2개의 수가 있다.
# ...
# 두 개의 n 사이에는 정확히 n개의 수가 있다.
# 예를 들어 3, 1, 2, 1, 3, 2은 n=3인 랭퍼드 수열이다.
#
# n이 주어졌을 때, 길이 2n의 랭퍼드 수열의 개수를 구하면 된다. 하지만 이렇게만 하면 재미가 없으니 조건 하나를 추가하고자 한다. x번째 수와 y번째 수는 같다는 조건이다. (이 번호는 1부터 시작한다.)
#
# 입력
# 세 자연수 n, x, y가 주어진다. (2 ≤ n ≤ 12, 1 ≤ x < y ≤ 2n, 1 ≤ y-x-1 ≤ n)
#
# 출력
# x번째 수와 y번째 수가 같은 길이 2n의 랭퍼드 수열의 개수를 출력한다.
#
# 예제 입력 1
# 3 1 5
# 예제 출력 1
# 1
# 예제 입력 2
# 7 4 10
# 예제 출력 2
# 4
# 예제 입력 3
# 12 1 3
# 예제 출력 3
# 19776
# 출처
# High School > 선린인터넷고등학교 > 제2회 천하제일 코딩대회 C번
from itertools import permutations


def solution(n, x, y):
    answer = 0
    array = []
    for i in range(1, n + 1):
        array.append(i)
        array.append(i)

    perarray = set(list(permutations(array, 2 * n)))
    xequalyarray = []
    # x와 같은지 판별
    for i in perarray:
        if i[x - 1] == i[y - 1]:
            xequalyarray.append(i)
    # print(xequalyarray)

    # 랭퍼든 수열 판별

    for i in xequalyarray:
        truenum = 0
        # 1부터 n까지 반복
        for j in range(1, n + 1):
            indexes = 0
            # 인덱스 담는곳
            indexlist = []
            # n과 배열의 숫자가 같은걸찾기 위해 반복
            for k in i:
                if j == k:
                    # n과 배열안의 숫자가 같을때 인덱스를 추가
                    indexlist.append(indexes)
                indexes += 1
            # n의 인덱스 - n의 인덱스는 = n+1
            if abs(indexlist[0] - indexlist[1]) != j + 1:
                truenum = 1

                break
        if truenum == 0:
            answer += 1

    return answer


n, x, y = 3, 1, 5

n, x, y = map(int, input().split())

print(solution(n, x, y))
