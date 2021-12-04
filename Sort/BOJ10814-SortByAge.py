#나이순 정렬 
# https://www.acmicpc.net/problem/10814

def solution(array):


	return sorted(array, key = lambda x : (int(x[0]), x[2]) )

number = int(input())

# print(list([2,3]+3))

humanList = [list((input()+' '+str(i)).split()) for i in range(number)]



for listElement in solution(humanList):
	print(*listElement[:2:])

