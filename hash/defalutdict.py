# value 가 없어도 dictionary 생성 가능
# 초기 생성 인자에 따라 default value 값이 달라짐
from collections import defaultdict
a = defaultdict(int)
print(a)

b= defaultdict(list)
print(b)

c = defaultdict()
print(c)

print(a['cocojelly'])
print(b['cocojelly'])
