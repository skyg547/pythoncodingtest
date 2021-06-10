# https://www.acmicpc.net/problem/9252
# LCS2


def solution(l, s):
    answerArray  = []
    for i in l:
        answerArray.append(i)
        for i in s:
            answerArray.append(i)

    return answerArray

if __name__ == '__main__':
    l = 'ACAYKP'
    s = 'CAPCAK'

    print(solution(l, s))
