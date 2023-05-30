# 공부한 시간을 기록

# 1. 시작 버튼 : 공부를 시작할때의 시각을 기록
# 2. 중지버튼 공를 중지할때의 시각을 기록

# 다음과같은 규칙

# 1. 공부를 시작하고 5분이 지나기전에 중지 했다면 공부한 시간 포함 X
# 2. 공부를 시작하고 1시간 45이 넘어서 중비했다면 1시간 45분 까지 시간 인정 (1:45)

# . 공부를 시작한 시각과 중지한 시각이 연속적으로 주어짐


# 처음 주어진 시각은 무조건 공부를 시작한 시각
# 마지막 시각은 공부를 중지한 시각
# 차례대로 번갈아 가면서 시작 중지 시작 중지 중지 시각

# 이때 실제로 공부한 시간을 구하려 합니다
# log 매개 변후
# 실제로 공부한 시간을 HH MM 형태로 return 하도록 solution 함수를 완성

# log의 길이는 짝수입니다.
# 2 ≤ log의 길이 ≤ 1,440
# log의 원소는 시각을 나타내며 길이는 항상 5입니다.
# 시각은 항상 시:분을 뜻하는 HH:MM 형태로 주어집니다.
# 잘못된 시각은 주어지지 않습니다.
# 중복된 시각은 주어지지 않습니다.
# 시각은 오름차순으로 주어지며, 모두 같은 날 기록한 내용만 주어집니다.

def solution(log):
    startTime = 0
    studyTime = 0

    for index, timeLog in enumerate(log):
        if (index % 2) == 0:
            startTime = int(timeLog[0:2]) * 60 + int(timeLog[3:5])
        else:
            detailStudyTime = int(timeLog[0:2]) * 60 + int(timeLog[3:5]) - startTime
            if detailStudyTime < 5:
                detailStudyTime = 0
            elif detailStudyTime > 105:
                detailStudyTime = 105
            studyTime += detailStudyTime

    answer = str(studyTime // 60).zfill(2) + str(":") + str(studyTime % 60)
    return answer


if __name__ == '__main__':
    solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"])
