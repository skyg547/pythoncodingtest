# 준은 회사의 촐퇴근 시간을 잘활용하여 해외여행은 금요일에 출발하여 다음 월요일에 돌아오도록 여행일정을 세웁니다.

# 월 , 출 1  퇴 6
# 금 출 9:30 퇴 6

# 남은 휴가시간을 고려하지 않은 채
# 비행기 시간만 고려하여 여행 일정을 세웠다.

# 올해 남은 휴가시간 time 과 여행일정을 담은 plan

# 남은 휴가 시간 내에 갈수 있는 여행지 중 준의 올해 마지막 여행지가 어디 인지 return
#
# 1 ≤ plans의 길이 ≤ 1,000
# plans의 원소는 여행지, 출발 시간, 도착 시간 형식입니다.
# 여행 일정은 겹치지 않으며 계획 순서대로 이루어져 있습니다.
# 여행지는 길이가 1 이상 30 이하인 문자열입니다.
# 출발 시간과 도착 시간은 12시간제로 표기하며 길이가 3 이상 4 이하인 문자열입니다.

# 출발 시간과 도착 시간의 최소 단위는 1시간입니다.

# 출발 시간은 금요일이 기준이며, 도착 시간은 다음 월요일이 기준입니다.

# 오전은 "AM", 오후는 "PM"으로 표기합니다.

# time의 0.5는 30분을 의미하며, time의 최소 단위는 30분입니다.

# 회사에서 공항까지 이동 시간, 점심시간은 고려하지 않습니다.

# 금  출 6시 , 월 도착 9시 30분
# 올해 마지막 여행지가 어디냐 ?

# plans는 계획 순서대로 이루어짐

# 여행지, 출발시간, 도착시간 형식
# 최소 한시간

# 금 토 일 월
def solution(time, plans):
    answer = ''

    # 퇴근 시간
    workTime = 18
    # 출근 시간
    workingTime = 13
    # 월욜일 최대 휴가 시간
    maxMorningVacationTime = 5
    # 금요일 최대 휴가 시간
    maxEveningVacationTime = 8.5

    for plan in plans:

        if plan[1][-2:] == 'AM':
            departurTime = int(plan[1][0:-2])
        else:
            departurTime = int(plan[1][0:-2]) + 12

        # 도착시간
        if plan[2][-2:] == 'AM':
            arriveTime = int(plan[2][0:-2])
        else:
            arriveTime = int(plan[2][0:-2]) + 12

        # 휴가 사용 시간 적용 시켜주기
        if 0 > workTime - departurTime:
            vacationForEvening = 0
        else:
            vacationForEvening = workTime - departurTime

        if 0 > arriveTime - workingTime:
            vacationForMorining = 0
        else:
            vacationForMorining = arriveTime - workingTime

        # 휴가 시간 계산 해주기
        time = time - min(maxMorningVacationTime, vacationForMorining) - min(maxEveningVacationTime, vacationForEvening)

        if time > 0:
            answer = plan[0]
        else:
            break

    return answer


if __name__ == '__main__':
    solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]])
