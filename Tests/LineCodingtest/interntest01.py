def solution(ads):
    answer = 0
    lostMoeny = [0] * 25001
    # 시간초는 5초
    s = 5

    ads.sort(key=lambda x: (x[0], x[1]))
    # print(ads)

    time = ads[0][0]+5

    # 5마다 끊어 줘서 배열에 넣어줘서 손해비용 갱신
    while ads:
        possbleAdTable = []

        for ad in ads:
            if ad[0] <= time:
                # 광고를 틀어줄거다
                possbleAdTable.append(ad)

        if len(possbleAdTable) == 1:

            time += 5
            i = ads.index(possbleAdTable[0])
            del ads[i]
            continue
# 최소 비용 산출
        else:

            if len(possbleAdTable) > 1:
                minCost = [0] * len(possbleAdTable)

                time += 5
                for i in range(len(possbleAdTable)):

                    minCost[i] = (time-possbleAdTable[i][0])*possbleAdTable[i][1]

                for i in possbleAdTable:

                    if max(minCost) == (time - i[0]) * i[1]:
                        indexs = ads.index(possbleAdTable[possbleAdTable.index(i)])
                        del ads[indexs]

                answer += sum(minCost)-max(minCost)

                # print(lostMoeny)
                continue

        time += 1

    # 고르기

    # (계산식은 광고 끝나는 시간  -  시작시간 )* 손해비용인데 이걸 비교

    # 그때 그때 다름

    # 시간 별로 정렬

    # 그다음 손해비용 별로 정렬

    # 아니며 모든 경우의수 확인 ?

    return answer


if __name__ == '__main__':
    l = [[0, 1], [0, 2], [6, 3], [8, 4]]
    s = [[5, 2], [2, 2], [6, 3], [9, 2]]
    print(solution(s))
