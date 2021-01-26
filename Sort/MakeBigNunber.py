# 큰수 만들기
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	6210
# [3, 30, 34, 5, 9]

# 시간초과
# from itertools import permutations
#
#
# def solution(numbers):
#     answer = ''
#
#     perm = list(permutations(numbers, len(numbers)))
#     print(perm)
#     tempanswer = []
#
#     for i in range(len(perm)):
#         s = ''
#         for j in range(len(perm[i])):
#             s = s + str(perm[i][j])
#         tempanswer.append(int(s))
#
#     answer = str(max(tempanswer))
#
#     return answer

# 실패 쪼개는게 아님
# def solution(numbers):
#     answer = ''
#     tempanswer = []
#     for i in numbers:
#         if i == 1000:
#             tempanswer.append(int(i/1000))
#             tempanswer.append(int(i%1000/100))
#             tempanswer.append(int(i%100/10))
#             tempanswer.append(int(i%10))
#         elif i >= 100:
#             tempanswer.append(int(i/100))
#             tempanswer.append(int(i%100/10))
#             tempanswer.append(int(i%10))
#         elif i >= 10:
#             tempanswer.append(int(i/10))
#             tempanswer.append(int(i%10))
#         else:
#             tempanswer.append(int(i))
#
#     tempanswer.sort(reverse=True)
#     print(tempanswer)
#     for i in tempanswer:
#         answer += str(i)
#     print(tempanswer)
#
#     return answer

# 정답
def solution(numbers):

    print(numbers)
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3,reverse=True)
    print(numbers)

    return str(int(''.join(numbers)))


numbers = [6, 10, 2,30,34]
print(solution(numbers))

# # e다른해설
# import functools
#
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
#
# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer