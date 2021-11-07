# rows 행 과 columns 열로 이루어진 격자가 있다

# 처음에 모든 격자 칸 안에는 숫자 0이 쓰여 있다 .

# 1. 현재 위치를 1행 1열로 정하고 그위치에 숫자 1을 쓴다.
# 2. r을 현재 위치의 행, c를 현재 위치의 열로 정의

# 만약 격자내에 0이 쓰인 칸이 없거나, 더이상 0이 쓰여있는 칸에 다른 숫자를 쓸수 없게 된다면 과정을 종료 한다. -> 종료 조건

# 만약 최근에 쓰인 숫자가 짝수 라면 r,c 에서 r+1 , c 로 이동  ->아래로 한칸  넘어가기 가능
# 만약 최근에 쓰인 숫자가 홀수 라면 r,c 에서 r, c+1 로 이동 -> 오른쪽으로 한칸  넘어가기 가능
# 도착한 칸에 원래 쓰여 있던 수를 지우고 (가장최근에 쓴 숫자 +1) 을 쓴다

# 2과정으로 돌아가기

def solution(rows, columns):
    answer = [list(0 for _ in range(columns)) for _ in range(rows)]

    nowLocation = [0, 0];

    number = 1
    checkIncluding = -1

    # 루틴 한번씩 반복
    while True:

        # 0 있는지 없는지 검사
        for row in answer:
            for cols in row:
                if cols == 0:
                    checkIncluding = 0
        if checkIncluding == -1:
            break
        # 다시 초기화
        checkIncluding = -1

        # 숫자 써주기
        answer[nowLocation[0]][nowLocation[1]] = number

        # 무한 루프 검사
        if rows == columns:
            if number == rows + columns:
                break

        # 다음칸으로 이동
        if number % 2 == 0:
            if nowLocation[0]+1 == rows:
                nowLocation[0] = 0
            else:
                nowLocation[0] += 1
        else:
            if nowLocation[1] + 1 == columns:
                nowLocation[1] = 0
            else:
                nowLocation[1] += 1

        # 숫자 더해주기
        number += 1

    return answer


if __name__ == '__main__':
    solution(3, 3)
