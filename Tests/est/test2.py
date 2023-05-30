def solution(scores):
    answer = 0

    # 점수환산
    scoreDict = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

    #지원자 수 반복
    for appicant in scores:
        # A 갯수
        countA = 0
        # B 갯수
        countF = 0
        # 점수 합산
        sumScore = []

        # 지원자의 점수 반복
        for score in appicant:
            if score == "A":
                countA += 1
            elif score == "F":
                countF += 1

            # 점수표 만큼 반복, 점수 환산
            for changedScore in scoreDict:
                if score == changedScore:
                    sumScore.append(scoreDict[changedScore])

        # 최고, 최저 제외 점수표 환산
        sumScore = (sum(sumScore) - max(sumScore) - min(sumScore)) / (len(sumScore) - 2)

        # 결과 계산 F > 2 탈락 A > 2 , 평균 >  3  합격
        if countF >= 2:
            continue
        elif countA >= 2 or sumScore >= 3:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["BCD", "ABB", "FEE"]))
