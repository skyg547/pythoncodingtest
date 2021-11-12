def solution(numberArray):
  numberArray.sort(key = -1)
  print(numberArray)
  
number = list(map(int, input().split()))

print(solution(number))
