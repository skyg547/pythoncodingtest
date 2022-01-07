#나이순 정렬 
# https://www.acmicpc.net/problem/10814

def solution(array):


<<<<<<< HEAD
	return sorted(array, key = lambda x : (x[0], x[2]) )


# print(solution([[21, "junky", 0], [22, "dogu", 1], [21, "ho", 2]]))
# 	return sorted(array, key = lambda x : (int(x[0]), int(x[2])) )
=======
	return sorted(array, key = lambda x : (int(x[0]), int(x[2])) )
>>>>>>> a9f2226b0caf86bc64dde4d2a0e0e24de4f36904

number = int(input())

# print(list([2,3]+3))

humanList = [list((input()+' '+str(i)).split()) for i in range(number)]



for listElement in solution(humanList):
	print(*listElement[:2:])

