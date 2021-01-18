# 사전 자료형 = 해시테이블
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
print(data['바나나'])

if '사과' in data:
    print("'사과'가 라는 키가 존재합니다")

key_list = list(data.keys())

value_list = data.values()

print(key_list)
print(value_list)

# 집합 자료형 = 해시셋
data = set([1, 1, 1, 2, 3, 4, 5])
print(data)

data = {1, 2, 3, 4, 5, 5, 6, 1, 6}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)

data = set([1, 2, 3])
print(data)
data.add(4)
print(data)
data.update([5, 6, 7, 8, 9])
print(data)
data.remove(3)
print(data)
