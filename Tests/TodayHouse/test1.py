from collections import deque


# x는 내비게이션이 안내 메시지를 보내는 시간
# 출발 직후 시간은 0
# 100m 이동 할때 마다 단위시간 1만큼
# y는 다음 방향  변경 ㅈ점 까지 직선거리
# dire 진행 방향 기준으로 바꾸어야 할 방향
# left or Right
# 문자 한개당 100m

# 갈때마다 1개 체크
# 방향 전화 직후 체크
# 제일 앞에꺼 체크

# EWSM

def solution(path):
    answer = []
    direction = {"NE": "right", "NW": "left", "EN": "left", "ES": "right", "SE": "left", "SW": "right", "WS": "left",
                 "WN": "right"}
    bearingPath = deque(path)

    time = 0
    checkTime = 0
    # 하나씩 뽑아준다
    while bearingPath:
        nowBearing = bearingPath.popleft()
        if checkTime > time:
            time += 1
            continue
        for nextTime, bearing in enumerate(bearingPath):
            if nextTime >= 5:
                break
            if bearing != nowBearing:
                answer.append(
                    "Time %s : Go straight %dm and turn %s" % (time, (nextTime + 1) * 100, direction[
                        nowBearing + bearing]))
                checkTime = (nextTime + 1) + time
                break
        time += 1
    return answer


if __name__ == '__main__':
    print(solution("SSSSSSWWWNNNNNN"))
