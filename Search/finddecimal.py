# # 소수 찾기
# # 문제 설명
# # 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# #
# # 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
# #
# # 제한사항
# # numbers는 길이 1 이상 7 이하인 문자열입니다.
# # numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# # 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# # 입출력 예
# # numbers	return
# # 17	3
# # 011	2
# # 입출력 예 설명
# # 예제 #1
# # [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
# #
# # 예제 #2
# # [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
# #
# # 11과 011은 같은 숫자로 취급합니다.
# import math
# from itertools import combinations
# from itertools import permutations
#
# a = (0,)
# print(len(a))
# _list = [1, 2, 3]
# perm = list(permutations(_list, 2))
# print(perm)
#
#
def is_prime_number(x):

    if x < 2: return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하여
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True

#
# #
# # _list = [1, 2, 3]
# # combi = list(combinations(_list, 2))
# # print(combi)  # [(1, 2), (1, 3), (2, 3)]
# # # 갯수 별로 조합을 반복할 수 있다.
# # for i in range(1, len(_list) + 1):
# #     print(list(combinations(_list, i)))
#
#
# # [(1,), (2,), (3,)]
# # [(1, 2), (1, 3), (2, 3)]
# # [(1, 2, 3)]
#
def solution(numbers):
    answer = 0
    for i in range(1, len(numbers) + 1):
        temp = (list(map(''.join,permutations(numbers, i))))
        for j in list(set(temp)):
            if is_prime_number(int(j)):
                answer += 1
    return answer



from itertools import permutations
import math


def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):

        perlist = list(map(''.join, permutations(list(numbers), k)))
        print(perlist,k)
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))
    return  answer


numbers = "018"
print(solution(numbers))
