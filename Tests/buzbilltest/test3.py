from itertools import combinations


def check(list, minLevel, maxLevel):
    for i in list:
        if i < minLevel:
            return False
        if i > maxLevel:
            return False
    return True


def countTeams(skills, minPlayers, minLevel, maxLevel):
    # Write your code here
    answercnt = 0
    for i in range(minPlayers, len(skills) + 1):
        templist = list(combinations(skills, i))
        for j in templist:
            if check(j, minLevel, maxLevel):
                answercnt += 1

    return answercnt


# 조합
skills = [248, 779, 392, 727, 561]
minPlayers = 2
minLevel = 360
maxLevel = 1000

print('answe', countTeams(skills, minPlayers, minLevel, maxLevel))
