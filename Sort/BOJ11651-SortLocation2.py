def solution(arr):
  return sorted(arr, key = lambda x : (x[0],x[1]))


print(solution([
(0, 4),
(1 ,2),
(1 ,-1),
(2 ,2),
(3 ,3)]))



5
0 4
1 2
1 -1
2 2
3 3