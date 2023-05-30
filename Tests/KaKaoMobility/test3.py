from collections import deque
from itertools import permutations
from itertools import combinations
import sys

input = sys.stdin.readline


# ABC DEFG HJK

# 2 : 2 가능

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# max
# 2
# 개
# min
# 1
# 개

from string import ascii_uppercase

def solution(N, S):
    # write your code in Python 3.8.10
    alphaBetMatchingToNumber = dict(map(lambda x: (x[1], x[0]), enumerate(ascii_uppercase[0:10:])))  # 좌석 열 숫자 변경
    needSeatGroup = {(1, 2, 3, 4), (5, 6, 7, 8), (3, 4, 5, 6)}  # 예약 해야하는 좌석
    seats = [[False] * len(alphaBetMatchingToNumber) for _ in range(N)]  # 좌석 목록
    reservaitonSeats = list(map(lambda x: (int(x[:-1:]) - 1, alphaBetMatchingToNumber[x[-1]]), S.split()))  # 예약 좌석 목록

    for reservaitonSeat in reservaitonSeats:  # 좌석 예약 처리
        seats[reservaitonSeat[0]][reservaitonSeat[1]] = True

    possibleReseveSeatCount = 0  # 예약 가능 좌석
    for seat in seats:  # 전좌석 돌기
        for needSeats in needSeatGroup:  # 필요한 좌석 돌기
            isReservedSeat = False
            for needSeatNumber in needSeats:  # 예약 유무 확인
                if seat[needSeatNumber]:
                    isReservedSeat = True
                    break
            if isReservedSeat:  # 이미 예약된 좌석
                continue  # 예약 실패
            for needSeatNumber in needSeats:  # 예약 처리
                seat[needSeatNumber] = True
            possibleReseveSeatCount += 1  # 예약가능

    print(possibleReseveSeatCount)


if __name__ == '__main__':
    solution(22, "1A 3C 2B 20G 5A")
