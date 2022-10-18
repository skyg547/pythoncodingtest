# https://www.acmicpc.net/problem/1748
# 수 이어 쓰기1
#
# 12345
# 123456789 10 11


if __name__ == '__main__':
    print(100000000)
    number = 15
    divideNumber = 10
    numberLength = 1
    answer = 0
    while number >= 1:
        answer += (number % divideNumber) * numberLength
        print(answer, number)
        numberLength += 1
        number //= divideNumber


    print(answer)
