# #주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
# ※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.

def solution(prices):
    answer = [ 0 for _ in range(len(prices))]
    stack = []
    stack.append([0,prices[0]])
    #스택에 인덱스 저장
    for i, value in enumerate(prices):
        if value < stack[-1][1]:
            answer[stack[-1][0]] += 1
            stack.pop()

        stack.append([i,value])
        #맨처음꺼 빼주기

        if i == 0:
            stack.pop()
        #print(stack)


        #스택에있는 인덱스는 1초씩 더하기
        for j in range(len(stack)):
            answer[stack[j][0]] += 1

    #맨처음 1초 빼주기
    for i in range(len(answer)):
        answer[i] = answer[i]-1


    print(answer)
    return answer



a = [5,8,6,2,4,1]
solution(a)


def solution1(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while len(stack) != 0 and prices[i] < prices[stack[len(stack) -1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    while len(stack):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1

    return answer