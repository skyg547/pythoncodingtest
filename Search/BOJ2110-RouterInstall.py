# https://www.acmicpc.net/problem/2110
# 공유기 설치
# 한 집에는 공유기를 하나
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게
# 가장 인접한 두 공유기 사이의 최대 거리를 출력

# 200,000

# 얼만큼
# 떨어진
# 곳에
# 두어야
# 하는지

import sys


def solution(l, C):
    start = 1

    # 끝에서 첫번째 사이 공유기를 설치 한다
    end = l[-1] - l[0]

    result = 0

    # 교차하면 종료
    while start <= end:

        # 중간 값
        mid = (start + end) // 2
        # 공유기가 있는 위치
        old = l[0]
        # 중간에 공유기를 하나 설치 했다
        count = 1

        # 반복문을 돌면서 설치할수 있는 공유기 갯수를  확인 해준다
        for i in range(1, len(l)):
            # 공유기를 설치 했을때 mid 거리안에 i의 집까지 전파가 닿지 않을 경우
            if l[i] >= old + mid:
                # 공유기를 하나 추가한다
                count += 1
                #공유기 최신화 ?
                old = l[i]

        # 설치 할수 있는 공유기 갯수가 크면  넓게 설치 해야한다
        if count >= C:
            start = mid + 1
            result = mid
        # 설치 할수 공유기 갯수가 작으면 좁게 설치 해야 한다
        else:
            end = mid - 1
    return result


if __name__ == '__main__':
    N, C = 5, 3
    l = [1,
         2,
         8,
         4,
         9]

    N, C = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(N)]

    l.sort()
    print(solution(l, C))
