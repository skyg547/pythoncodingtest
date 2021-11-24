def solution(numberArray):
    print(''.join(list(map(str,sorted(numberArray, reverse=True)))))


#
# number = list(map(int, input().split()))

number = list(input())

s = list(map(int, number))

solution(s)
