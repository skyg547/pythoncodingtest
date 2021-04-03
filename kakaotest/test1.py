def solution(lottos, win_nums):
    answer = []
    cnt = 0

    # 최저 처리
    for i in lottos:
        if i in win_nums:
            cnt += 1

    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)

        # 최고처리
    for i in lottos:
        if i == 0:
            cnt += 1

    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)

    answer.reverse()

    return answer


# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]
lottos, winnums = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]

print(solution(lottos, winnums))

# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외
