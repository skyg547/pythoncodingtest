def solution(inp_str):
    answer = []

    # 1번
    if len(inp_str) < 8:
        answer.append(1)
    elif len(inp_str) > 15:
        answer.append(1)

    # 2번
    alpaL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    alpaU = []
    for i in alpaL:
        alpaU.append(i.upper())

    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    spechar = ['~', '!', '@', '#', '$', '%', '^', '&', '*']

    for i in inp_str:
        if i not in alpaL:
            answer.append(2)
            break
        elif i not in alpaU:
            answer.append(2)
            break
        elif i not in number:
            answer.append(2)
            break
        elif i not in spechar:
            answer.append(2)
            break

        # 3번
    sumone = 0
    inp_str_U = ''.join(set(inp_str))
    print(any(inp_str_U))

    if any(inp_str_U) in alpaU and any(inp_str_U) in alpaL and any(inp_str_U) in number:
        pass

    elif any(inp_str_U) in alpaL and any(inp_str_U) in spechar and any(inp_str_U) in number:
        pass

    elif any(inp_str_U) in alpaU and any(inp_str_U) in spechar and any(inp_str_U) in number:
        pass

    elif any(inp_str_U) in spechar and any(inp_str_U) in alpaL and any(inp_str_U) in alpaU:
        pass
    else:
        answer.append(3)

    # print(inp_str_U)
    # for i in inp_str_U:
        # if i in alpaL:
        #     if sumone == 1:
        #         pass
        #     else:
        #         sumone += 1
        # elif i in alpaU:
        #     if sumone == 2:
        #         pass
        #     else:
        #         sumone += 2
        # elif i in number:
        #     if sumone == 3:
        #         pass
        #     else:
        #         sumone += 3
        # elif i in spechar:
        #     if sumone == 4:
        #         pass
        #     else:
        #         sumone += 4



    # 4번
    for i in range(len(inp_str)):

        if i >= len(inp_str) - 3:
            continue
        if inp_str[i] == inp_str[i + 1] and inp_str[i] == inp_str[i + 2] and inp_str[i] == inp_str[i + 3]:
            answer.append(4)
            break
    # 5번
    for j in inp_str:
        cnt = 0

        for i in inp_str:

            if cnt >= 5:
                answer.append(5)
                return answer

            if j == i:
                cnt += 1
    if not answer:
        return [0]
    return answer


inp_str = "ZzZz9Z824"
print(solution(inp_str))
