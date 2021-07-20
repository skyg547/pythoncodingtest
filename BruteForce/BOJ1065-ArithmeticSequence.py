# # https://www.acmicpc.net/problem/1065
# # 한수
#
#
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
#
def solution(n):
    cnt = 0;

    for number in range(11, n):

        if number >= 10:
            diffrens = abs(int(str(number)[1]) - int(str(number)[0]))
        else:
            cnt += 1
            continue

        firstElement = int(str(number)[0])
        breakPoint = 0
        for element in str(number):
            if str(number).index(element) == 0: # 여기서 에러
                continue

            if diffrens != abs(firstElement - int(element)):
                breakPoint = 1
                break
            firstElement = int(element)

        if breakPoint == 1:
            continue
        cnt += 1

    return cnt


if __name__ == '__main__':
    n = int(input())
    print(solution(n))

number = 111
diffrens = abs(int(str(number)[1]) - int(str(number)[0]))

firstElement = int(str(number)[0])

for element in str(number):
    if str(number).index(element) == 0:
        continue

    if diffrens != abs(firstElement - int(element)):
        print("x")
        break

    firstElement = int(element)
