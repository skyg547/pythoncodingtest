#나이순 정렬 

def solution(array):


	return sorted(array, key = lambda x : (x[0], x[2]) )


print(solution([[21, "junky", 0], [22, "dogu", 1], [21, "ho", 2]]))