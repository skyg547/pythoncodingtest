def solution(program, flag_rules, commands):
    answer = []

    alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    split_flag_rules = []
    split_command = []
    for i in range(len(commands)):
        answer.append(True)

    flag_name = []

    # 플래그 룰 리스트 만들기
    for i in range(len(flag_rules)):
        split_flag_rules.append(list(map(str, flag_rules[i].split())))

    # 커맨드 리스트 만들기
    for i in range(len(commands)):
        split_command.append(list(map(str, commands[i].split())))

    #플래그 네임 집합 만들기
    for i in range(len(split_flag_rules)):
        # print(split_flag_rules[i])
        for j in split_flag_rules[i]:
            # print(j)
            flag_name.append(j)
            break

    print(flag_name)
    for i in range(len(split_command)):
        print(split_command[i])
        for j in range(1, len(split_command[i])):
            # 플래그 이름 동등에 대한 처리
            print('*******',split_command[i][j])
            if split_command[i][j] in flag_name:
                if split_command[i][j] in flag_name:
                    pass
                else:
                    # answer[i] = False
                     # 플래그 타입 동등에 대한 처리
                    for h in flag_name:
                        print("hhhhhh",h)
                        if split_command[i][j - 1] == h:
                            for x in split_command[i][j]:
                                if x not in alpa:
                                    answer[i] = False
                                    print(2)

                # elif split_command[i][j - 1] == flag_name[1]:
                #     for h in split_command[i][j]:
                #         if h not in number:
                #             answer[i] = False
                #             print(3)
                #
                # elif split_command[i][j - 1] == flag_name[2]:
                #     if split_command[i][j] is not None:
                #         answer[i] = False
                #         print(4)



    # 프로그램명 동등에 대한 처리
    for i in split_command:

        if i[0] != program:
            answer[split_command.index(i)] = False
            print(5)

        else:
            pass
    return answer


p = "trip"
f = ["-days NUMBERS", "-dest STRING"]
c = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]

print(solution(p, f, c))
# [True, False]
