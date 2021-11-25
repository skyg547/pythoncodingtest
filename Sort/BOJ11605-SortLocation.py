def solution(locationArray):
  # locationArray.sort(lambda x : (x[0], x[1]))

  return sorted(locationArray, key =  lambda x : (x[0], x[1]))

number = int(input())

locations = [list(map(int, input().split())) for _ in range(number)]



for element in solution(locations):
  print(*element)