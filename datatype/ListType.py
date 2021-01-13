a = [1,2,3,4,5,6,7,8,9]
print(a)

print(a[3])

n = 10
a = [0,2] * n
print(a)

print(a[-1])

a = [1,2,3,4,5,6,7,8,9]

print(a[7])

print(a[-1])

print(a[-3])

a[3] = 7
print(a)

a[-4] = 999
print(a)

a = [1,2,3,4,5,6,7,8,9]

print(a[3])

print(a[1:4])

array = [i for i in range(10)]

print(array)

array = [i for i in range(20) if i%2 == 1]

print(array)

array = [i*i for i in range(1,10)]

print(array)

#nxm 크기의 2차원 리스트 초기화

n = 4
m = 3
array = [[0]*m for _ in range(n)]
print(array)

# 잘못된 방법

# _ 변수의 값을 무시 하기 위해 언더바 사용

summary = 0
for i in range(1, 10):
    summary += i

print(summary)

for _ in range(5):
    print("Hello World")

# append() 리스트 원소 삽입
# sort() 정렬 오름차순 sort(reverse = True) 내리차숨
# insert() 특정한 인덱스 원소삽입
# count 특정값 개수 셀때
# remove() 특정값 제게ㅔ


a = [1,4,3]
print("기본 리스트 :", a)

a.append(2)
print("삽입: ",a )

a.sort()
print("오름 차순 정렬: ", a)

a.sort(reverse=True)
print("내리차순 정렬 : ", a)

a.reverse()
print("원소 뒤집기: ",a)

a.insert(2,3)
print("인덱스에 2에 3추가" ,a)

print("3이 갯수 값 ㅅ세기" , a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제:" , a)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)