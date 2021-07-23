# # # https://www.acmicpc.net/problem/1065
# # # 한수
# #
# #
# # 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# #
# #
# def solution(n):
#     cnt = 0;
#
#     for number in range(n):
#
#         if number >= 100:
#             diffrens = abs(int(str(number)[1]) - int(str(number)[0]))
#         else:
#             cnt += 1
#             continue
#
#         firstElement = int(str(number)[1])
#         breakPoint = 0
#         for index, element in enumerate(str(number)):
#             if index == 0 and index == 1:  # 여기서 에러
#                 # print(index)
#                 continue
#             if diffrens != firstElement - int(element):
#                 breakPoint = 1
#                 break
#             firstElement = int(element)
#
#         if breakPoint == 1:
#             continue
#         cnt += 1
#
#     return cnt
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print(solution(n))
# #
# # number = 111
# # diffrens = abs(int(str(number)[1]) - int(str(number)[0]))
# #
# # firstElement = int(str(number)[0])
# #
# # for element in str(number):
# #     if str(number).index(element) == 0:
# #         continue
# #
# #     if diffrens != abs(firstElement - int(element)):
# #         print("x")
# #         break
# #
# #     firstElement = int(element)
#
#
num = int(input())
hansu = 0

for n in range(1, num + 1):
    if n <= 99:  # 1부터 99까지는 모두 한수
        hansu += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
            hansu += 1