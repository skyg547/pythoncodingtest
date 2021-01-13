#모험가 길드

n = int(input())
data = list(map(int, input().split()))
data.sort() # 공포도 순으로 오름차순 !! 중요


result = 0 #총 그룹의 수
count = 0 # 현재 그룹에 포합된 모험가의 수

for i in data: #공포도 낮은 순부터 확인
    count += 1 # 현재 파티 결성
    if count >= i: # 현재 파티원수와 공포도 확인
        result += 1 # 총그룹수 추가
        count = 0  # 현재 파티원 초기화

print(result)