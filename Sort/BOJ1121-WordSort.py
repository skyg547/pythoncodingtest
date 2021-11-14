def solution(arrays):

  
  return sorted(arrays, key = lambda x : (-len(x), min(x)))


print(["ab","cd","b"])