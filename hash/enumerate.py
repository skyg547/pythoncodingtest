# enumerate object는 인덱스를 포함함
# 인자로 iterable이 와야함
# for 문과 함께 많이 사용됨

season = ['spring', 'summer', 'fail', 'winter']

print(enumerate(season))

i = list(enumerate(season))
print(i)

l = list(enumerate(season, start=1))
print(l)

for i in enumerate(season):
    print(i)
