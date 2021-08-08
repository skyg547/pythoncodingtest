# # https://www.acmicpc.net/problem/5622
# # 다이얼
#
# 단어 갯수마다 2초 곱하기
# 아스키 코드로 빼주기

# 정규 표현식

import re

# ABC
# DEF
#

p = [
    re.compile('[a-c]', re.IGNORECASE),
    re.compile('[d-f]', re.IGNORECASE),
    re.compile('[g-i]', re.IGNORECASE),
    re.compile('[j-l]', re.IGNORECASE),
    re.compile('[m-o]', re.IGNORECASE),
    re.compile('[p-s]', re.IGNORECASE),
    re.compile('[t-v]', re.IGNORECASE),
    re.compile('[w-z]', re.IGNORECASE)]

answer = 0
strings = input()

for char in strings:
    # print(char)
    for index, element in enumerate(p):
        if element.match(char):
            answer += (index + 3)
            break

print(answer)

#
# print(str(p))
# print(p.search('ca'))
#
# print(ord('U') - ord('A'))
# print(ord('U'))
# print(ord('A'))
