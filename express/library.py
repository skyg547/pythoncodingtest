import math
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
from collections import  Counter


#내장함수 기본 입출력 함수, 정렬함수

#sum
result = sum([1,2,3,4,5])
print(result)

#min(),max()

min_result = min(7,3,2,1)
max_result = max(4,2,5,8)
print(min_result, max_result)

# eval() 사람의 입장에서 계산
result = eval("(3+5)*7")
print(result)

#sorted()

result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

#sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개',50)]
result = sorted(array, key= lambda x: x[1], reverse=True)
print(result)

#itertools 순열, 조합, 반복되는 형태 라이브러리 처리

#순열
data = ['A','B','C']
result = list(permutations(data,3))
print(result)

#조합
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

#중복 순열
data = ['A','B','C']
result = list(product(data,repeat=2))
print(result)

#중복 조합
data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)

# Counter 라이브러리
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(counter)

#heapq 힙 자료구죠, 다익스트라, 우선순위 큐

#bisect 이진탐색 기능

#collections 덱, 카운터

#math 팩토릴얼 제곱근, 최대공약수, 삼각함수 , 파이
def lcm(a, b):
    return  a*b // math.gcd(a, b)

a = 21
b = 24

print(math.gcd(21, 14))# 최대공약수 계산
print(lcm(21, 14)) #최소공배수 계산