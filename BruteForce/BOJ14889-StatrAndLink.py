# https://www.acmicpc.net/problem/14889
# 스타트와 링크

from itertools import combinations

def solution(l):
    member = [i for i in range(len(l))]
    teams = []

    mins = 1e9

    for team in list(combinations(member, len(l) // 2)):
        teams.append(team)

    for i in range(len(teams) // 2):
        team = teams[i]
        sumA = 0
        for j in range(len(l) // 2):
            members = team[j]
            for k in team:
                sumA += l[members][k]

        team = teams[-i-1]
        sumB = 0
        for j in range(len(l) // 2):
            members = team[j]
            for k in team:
                sumA += l[members][k]

        mins = min(mins, abs(sumA - sumB))


    return mins

if __name__ == '__main__':
    l = 4
    s = [[0, 1, 2, 3],
         [4, 0, 5, 6],
         [7, 1, 0, 2],
         [3, 4, 5, 0]]

    print(solution(s))
