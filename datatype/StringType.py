data = 'hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a + " " + b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])
# 특정 인덱스의 문자를 바꾸는건 불가능

# 튜플 자료형 : 한번 선언하면 변경 불가능
a = (1,2,3,4,5,6,7,8,9)

print(a[3])

print(a[1:4])

a = (1,2,3,4)
print(a)

# a[2] = 8
# -> 서로 다른 성질의 데이터를 묶어서 관리해야 할때 사용
# -> 해싱 키값으로 사용
# -> 리스트보다 메모리 효율적 사용