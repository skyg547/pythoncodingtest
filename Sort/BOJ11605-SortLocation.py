def solution(locationArray):
  locationArray.sort(lamda:x->(x[0], x[1]))


number = int(input())

locations = [list(map(int, input())) for _ in range(number)]
