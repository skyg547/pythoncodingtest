#나이순 정렬 
# https://www.acmicpc.net/problem/10814

def solution(array):


	return sorted(array, key = lambda x : (x[0], x[1]) )

number = int(input())

humanList = [list(input().split()) for _ in range(number)]

for listElement in solution(humanList):
	print(*listElement)

