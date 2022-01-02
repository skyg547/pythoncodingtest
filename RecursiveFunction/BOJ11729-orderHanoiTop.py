# 하노이 탑 순서 https://www.acmicpc.net/problem/11729

move = []

def hanoi(n,a,b,c):
    if n==1:
        move.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)

def solution(number):
    answerList = []
    hanoi(number,1,2,3)
    print(len(move))
    print(move)
    return answerList


if __name__ == '__main__':

    print(solution(3))