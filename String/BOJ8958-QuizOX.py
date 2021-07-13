# https://www.acmicpc.net/problem/8958
# OX퀴즈

def solution(l):
    answer = []
    for element in l:
        cnt = 0;
        sumAns = 0;
        for charter in element:
            if charter == 'O':
                cnt += 1
                sumAns += cnt
            else:
                cnt = 0
        answer.append(sumAns)

    return answer


if __name__ == '__main__':
    n = int(input())
    l = [input() for _ in range(n)]

    for printe in (solution(l)):
        print(printe)
