# 알파벳 출력하기 - string 모듈
# 이번 강의에서는
#
# 모든 대문자를
# 또는 모든 소문자를
# 또는 모든 대소문자를
# 또는 숫자를
# 가져오는 방법을 배웁니다.
#
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 a부터 z까지의 소문자를 가져오려고 할 때, 'abcdefg ....'와 같이 손수 알파벳을 입력하곤 합니다.
#
# answer = 'abcdefghijk (편의상 생략)'
# 파이썬에서는
# 파이썬은 이런 데이터를 상수(constants)로 정의해놓았습니다.

import string

print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters) #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 숫자 0123456789
