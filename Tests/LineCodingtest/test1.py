def solution(table, languages, preference):
    answer = ''
    answertemp = []

    for h in range(len(table)):
        temnum = 0
        print(h)
        print(list(map(str, table[h].split())))
        temp = list(map(str, table[h].split()))
        for k in range(1, len(temp)):

            if temp[k] in languages:
                # print(temp[k])
                # print(abs(6 - k))
                for i in range(len(languages)):
                    if temp[k] == languages[i]:
                        # print('pre lllllllll', preference[i])
                        temnum = temnum + (abs(6 - k) * preference[i])

        print("---------", temnum)
        answertemp.append([temp[0], temnum])

    print(answertemp)
    answermax = 0
    for i in answertemp:
        if answermax == i[1]:
            answer = min([answer,i[0]])
        elif i[1] > answermax :
            answermax = i[1]
            answer = i[0]

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]

pre = [7, 5]

print(solution(table, languages, pre))
