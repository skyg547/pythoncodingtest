# https://www.acmicpc.net/problem/14501
# 퇴사.

if __name__ == '__main__':
    retireDate = int(input())
    interviews = sorted([[date + 1] + list(map(int, input().split())) for date in range(retireDate)], reverse=True,
                        key=lambda x: x[0])
    dateMaxProfits = [0] * (retireDate + 3)
    # print(interviews)
    # print(dateMaxProfits)
    for interview in interviews:
        if interview[0] + (interview[1] - 1) > retireDate:  # 은퇴날짜보다 크면 생략
            continue
        # 비교 해야 한다면
        # print(interview, dateMaxProfits)
        if interview[1] < 2:
            dateMaxProfits[interview[0]] = dateMaxProfits[interview[0] + 1] + (interview[2])
        else:
            dateMaxProfits[interview[0]] = dateMaxProfits[interview[0] + interview[1]] + \
                                           (interview[2]  # 비교, 현재 날짜 값 vs 추가 시간뒤 이득 값
                                            if interview[2] >  # 이득
                                               (dateMaxProfits[interview[0] + 1]  # 다음날 이득 최대값
                                                - dateMaxProfits[interview[0] + interview[1]])  # 마지막날 이득 최대값
                                            else dateMaxProfits[interview[0] + interview[1] - 1])

    # print(interview)
# print(dateMaxProfits)
print(dateMaxProfits[1])
