# https://www.acmicpc.net/problem/1026
# 숫자카드

if __name__ == '__main__':

    n = int(input())
    firstCards = sorted(list(map(int, input().split())))
    secondCards = sorted(list(map(int, input().split())), reverse=True)
    sumAnswer = 0
    for cardIndex in range(n):
        sumAnswer += (firstCards[cardIndex] * secondCards[cardIndex])
    print(sumAnswer)