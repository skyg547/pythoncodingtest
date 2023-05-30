# # 한변의 길이가 1인 정삼각형 n**2 으로 구성된 격자가 있다
#
# # 격자의 각 칸에는 문자 하나가 쓰여있다.
#
# # 격자를 시계방향 또는 반시계 방향으로 120도 회전하고자 함
#
# # 격자의 정보 grid
#
# # 회전 방향 clockwise
#
# # clockwise 가 의미하는 방향으로 회전시킨 결과를 배열에 담아 return
#
# 1 ≤ grid의 길이 ≤ 1,000
# grid[i]의 길이 = 2 * i + 1
# grid[i]는 영어 대소문자 또는 숫자로 이루어진 문자열입니다.
# clockwise가 참이면 시계 방향, 거짓이면 반시계 방향으로 120도 회전해야 함을 의미합니다.

def solution(grid, clockwise):
    answer = [list(0 for _ in range(2 * index + 1)) for index in range(len(grid))]

    gridLength = len(grid)

    print(answer)
    # 시계
    if clockwise:

        for xindex, row in enumerate(answer):
            for yindex, col in enumerate(row):
                # if :
                answer[gridLength - 1][2 * gridLength - 2] = grid[xindex][yindex]
            # elif 2:
            #     2
            # else 3:
            #     3

    return answer


if __name__ == '__main__':
    solution(["1", "234", "56789"], True)
