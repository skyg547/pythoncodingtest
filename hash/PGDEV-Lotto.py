def solution(lottos, win_nums):
    answer = []

    min_num = len(set(set(lottos) & set(win_nums)))

    cnt = 0

    for index in lottos:
        if index == 0:
            cnt += 1

    max_num = min_num + cnt

    # 1	6개 번호가 모두 일치
    if max_num == 6:
        answer.append(1)

    # 2	5개 번호가 일치
    elif max_num == 5:
        answer.append(2)
    # 3	4개 번호가 일치
    elif max_num == 4:
        answer.append(3)
    # 4	3개 번호가 일치
    elif max_num == 3:
        answer.append(4)
    # 5	2개 번호가 일치
    elif max_num == 2:
        answer.append(5)
    # 6(낙첨)	그 외
    else:
        answer.append(6)
    # 1	6개 번호가 모두 일치
    if min_num == 6:
        answer.append(1)

    # 2	5개 번호가 일치
    elif min_num == 5:
        answer.append(2)
    # 3	4개 번호가 일치
    elif min_num == 4:
        answer.append(3)
    # 4	3개 번호가 일치
    elif min_num == 3:
        answer.append(4)
    # 5	2개 번호가 일치
    elif min_num == 2:
        answer.append(5)
    # 6(낙첨)	그 외
    else:
        answer.append(6)


    return answer





if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    print(solution(lottos, win_nums))
