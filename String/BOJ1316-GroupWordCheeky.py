# # https://www.acmicpc.net/problem/1316
# # 그룹단어체키
# #
# # def solution(word):
# #     answer = 0
# #     # for element in word:
# #     #     if element i
# #
# #     answerSet = set()
# #     temp = ""
# #     word = "abab"
# #
# #     for element in word:
# #         answerSet.add(element)
# #         answerSet.add(temp)
# #     # 1.  dusthr
# #     # 나온적 있으면 set 추가
# #     # 모든 나온걸 set 에 추가 하고 검사하자
# #     # 들어있느지 안들어 있는지
# #     return answer
# #
# # if __name__ == '__main__':
# #
# #     loop = int(input())
# #     count = 0
# #
# #     for _ in range(loop):
# #         count += solution(input())
# #
# #     print(count)
# import re
#
# # 정답
# #n = 0
#
# #group_word = 0
#
# #for _ in range(n):
# #    word = input()
#     error = 0
#     for index in range(len(word) - 1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
#         if word[index] != word[index + 1]:  # 연달은 두 문자가 다른 때,
#             new_word = word[index + 1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
# #                error += 1  # error에 1씩 증가.
#  //   if error == 0:
# #        group_word += 1  # error가 0이면 그룹단어
#
# # print(group_word)
#
#
# strings = 'aaabbb'
# print(strings)
# reg = '*[a-zA-Z]'
# re.compile(reg)
#
# # print((re.findall(reg, strings)))

if __name__ == '__main__':
    3
    happy
    new
    year