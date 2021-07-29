# # https://www.acmicpc.net/problem/5622
# # 다이얼
#
# 단어 갯수마다 2초 곱하기
# 아스키 코드로 빼주기

# 정규 표현식

import re

p = re.compile('ab*')
print(str(p))
print(p.search('ca'))

print(ord('U')-ord('A'))
print(ord('U'))
print(ord('A'))