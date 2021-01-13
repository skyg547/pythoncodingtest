# 왕실의 나이트 문제

# 현재 나의트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


#8가지 방향에 대해서 이동이 가능 한지 확인

count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
        next_row = row+step[0]
        next_column = column + step[1]
    # 해당위치 이동 가능한지 카운드
        if next_row >=1 and next_row <=8 and next_column >= 1 and next_column <= 8:
            count += 1

print(count)
