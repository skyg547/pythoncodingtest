# 대학생 철수는 새 학기를 맞아 대학 수업 시간표를 만들려고 합니다. 철
#
# 수는 이번 학기에 총 5가지 과목을 듣고자 하며,
#
# 각 과목은 4개의 분반으로 나누어져 있습니다.
#
# 즉 1번 과목은 ‘A’분반, ‘B’분반, ‘C’분반, ‘D’분반으로 나누어져 있고, 2,3,4,5번 과목 또한 각각 ‘A’분반, ‘B’분반, ‘C’분반, ‘D’분반으로 나누어져 있습니다.
#
# 과목별로 각 분반은 서로 다른 교수님이 강의 하므로,
#
# 각 분반의 수업 시간은 서로 다를 수도 있고, 겹칠 수도 있습니다.
# 철수는 5가지 과목을 모두 들을 수 있도록
#
# 각 과목마다 4개의 분반 중 하나씩을 선택하여
#
# 시간표를 만들려 합니다.
#
# 예를 들어 5개의 과목 분반들의
#
# 수업 시간이 서로 다른 과목 분반들의 수업 시간과
#
# 전혀 겹치지 않는다면,
#
# 철수가 만들 수 있는 시간표는 총 1024(=4 x 4 x 4 x 4 x 4)가지입니다.
#
# 하지만 어떤 과목의 분반이 다른 과목의 분반과
#
# 수업 시간이 서로 겹치게 된다면 만들 수 있는
#
# 시간표의 가짓수는 줄어들게 됩니다.
#
# 철수가 만들 수 있는 올바른 시간표는 몇 개인지를 구하려고 합니다
#
# . 올바른 시간표란, 듣고자 하는 5개의 과목 중
# 어떤 과목도 다른 과목과 수업 시간이 겹치지 않는 시간표를 말합니다.
#
# 분반의 수업 시작 시각을 과목별로 담은 2차원 문자열 배열 schedule이 매개변수로 주어집니다. 만들 수 있는 올바른 시간표의 개수를 return 하도록 solution 함수를 완성해주세요.

# 모든 과목 분반의 수업 시간은 1주일에 3시간입니다. 1주일에 한 번, 3시간 연속으로 진행되거나 1주일에 두 번, 1시간 30분씩 진행됩니다.
# 수업이 끝나는 시각과 다른 수업이 시작하는 시각이 같더라도 수업 시간이 겹치지 않는 것으로 간주합니다.

# 한 과목 분반의 수업 시작 시간이 같을 수도 있습니다.

# 예를 들어, 한 과목의 4개의 분반이 모두 같은 시각에 시작할 수도 있습니다.

# 1개거나 3 시간  2개 1시간 반
#  h 9 - 18
#

from itertools import product


def solution(schedule):
    dayChangeMap = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4}
    day = []

    # 날짜 배열 딕셔너리 초기화
    for _ in range(len(schedule)):
        time = {}
        for clock in range(90, 211, 5):
            time[clock] = 0
        day.append(time)

    failTime = 0  # 실패 스케줄

    # 모든 스케줄 경우의수
    tempSchedules = list(product(*schedule))
    for tempSchedule in tempSchedules:  ## 임시 스케줄을 돌면서
        nextSchedule = True  # 다음 스케줄이 맞는지 확인

        for classTime in tempSchedule:  ## 과목 시간들을 확인 한다

            classPartTime = classTime.split()
            tempday = 0  # 임시 날짜
            for partTime in classPartTime:  ## 과목 시간이 여러 일 경우를 위해 반복면
                if partTime in dayChangeMap.keys():  # 날짜 인지 구분 한다.
                    tempday = dayChangeMap[partTime]  # 날짜 입력
                else:
                    timeclass = int(partTime.replace(":30", "5").replace(":00", "0"))

                    if len(classPartTime) > 2:  # 2보다 클때 1시간 30분
                        # 1시간 30분 이전 까지 빈 과목이라면 1로 채워주고
                        if day[tempday][timeclass] == 0 and day[tempday][timeclass + 5] == 0 and day[tempday][
                            timeclass + 10] == 0:
                            day[tempday][timeclass] = 1
                            day[tempday][timeclass + 5] = 1
                            day[tempday][timeclass + 10] = 1
                        # 아니라면 실패 시킨다
                        else:
                            failTime += 1
                            nextSchedule = False

                    else:  # 과목이 2개라 3 시간 일때 3시간 전까지 체크 해주고
                        if day[tempday][timeclass] == 0 \
                                and day[tempday][timeclass + 5] == 0 \
                                and day[tempday][timeclass + 10] == 0 \
                                and day[tempday][timeclass + 15] == 0 \
                                and day[tempday][timeclass + 20] == 0 \
                                and day[tempday][timeclass + 25] == 0:
                            day[tempday][timeclass] = 1
                            day[tempday][timeclass + 5] = 1
                            day[tempday][timeclass + 10] = 1
                            day[tempday][timeclass + 15] = 1
                            day[tempday][timeclass + 20] = 1
                            day[tempday][timeclass + 25] = 1
                        else:
                            failTime += 1
                            nextSchedule = False
                    tempday = 0  # 날짜 를초기화

                    if not nextSchedule:  # 실패 한 경우라면 탈출
                        break

            if not nextSchedule:
                break
        # 날짜 배열 딕셔너리 초기화
        day = []
        for _ in range(len(schedule)):
            time = {}
            for clock in range(90, 211, 5):
                time[clock] = 0
            day.append(time)

    return len(tempSchedules) - failTime


if __name__ == '__main__':
    print(solution(  # 행 과목수 , 열 # 과목별 분반
        [["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"],
         ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"],
         ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"],
         ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"],
         ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))
