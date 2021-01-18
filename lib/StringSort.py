# 문자열 정렬하기 - ljust, center, rjust
# 이번 강의에서는 문자열을 좌측/가운데/우측 정렬하는 법을 배워봅니다. 예시)
#
# '가나다라               ' # 좌측정렬
# '               가나다라' # 우측 정렬
# '       가나다라        ' # 가운데 정렬
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 기존 스트링에 공백문자 (' ') 를 여러 번 붙이는 번거로운 일을 하지요. 이렇게요!
#
# ### 우측 정렬 예
# s = '가나다라'
# n = 7
#
# answer = ''
# for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
#     answer += ' '
# answer += s
# 파이썬에서는
# 파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.

s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
print(s.ljust(n))
s.center(n) # 가운데 정렬
print(s.center(n))

s.rjust(n) # 우측 정렬
print(s.rjust(n))
