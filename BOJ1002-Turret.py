# # 터렛
# # https://www.acmicpc.net/problem/1002
# import math
import math

if __name__ == '__main__':
    n = int(input())
    inputCase = [list(map(int, input().split())) for _ in range(n)]

    for location in inputCase:
        distation = math.dist((location[0], location[1]), (location[3], location[4]))
        if distation == 0 and location[2] - location[5] == 0: # 일치할때
            print(-1)
        elif abs(location[2] - location[5]) == distation or location[2] + location[5] == distation:  # 내접 외접
            print(1)
        elif location[2] + location[5] > distation > abs(location[2] - location[5]):  # 사이 낀거
            print(2)
        else:
            print(0)  # 접촉을 안할대
