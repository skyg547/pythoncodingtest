# https://www.acmicpc.net/problem/14501
# 퇴사.

if __name__ == '__main__':
    retireDate = int(input())
    interviews = sorted([[date + 1] + list(map(int, input().split())) for date in range(retireDate)], reverse=True,
                        key=lambda x: x[0])
    dateMaxProfits = [0] * (retireDate + 3)
    for interview in interviews:
        if interview[0] + (interview[1] - 1) > retireDate:  # 은퇴날짜보다 이전꺼
            dateMaxProfits[interview[0]] = dateMaxProfits[interview[0] + 1]
        else:
            dateMaxProfits[interview[0]] = max(interview[2] + dateMaxProfits[interview[0] + interview[1]],
                                               dateMaxProfits[interview[0] + 1])

print(dateMaxProfits[1])
