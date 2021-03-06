# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 나머지와 몫을 따로 구합니다
#
# a = 7
# b = 5
# print(a//b, a%b)
# 파이썬에서는
# 파이썬의 divmod와 unpacking을 이용하면 다음과 같이 코드를 짤 수 있습니다.

a = 7
b = 5
print( *divmod(a, b) )
# ⨳ divmod를 사용할 때 주의할 점
# 본 부가 설명은 [partrita](partrita@gmail.com) 님의 제보로 추가됐습니다.
#
# 무조건 divmod를 사용하는 게 좋은 방법은 아닙니다.
# 가독성이나, 팀의 코드 스타일에 따라서, a//b, a%b와 같이 쓸 때가 더 좋을 수도 있습니다.
# 또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.
