# 테트로미노 분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	37976	13972	9021	34.779%
# 문제
# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
#
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
#
#
#
# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
#
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
#
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
#
# 입력
# 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
#
# 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.
#
# 출력
# 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
#
# 예제 입력 1
# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1
# 예제 출력 1
# 19
# 예제 입력 2
# 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 예제 출력 2
# 20
# 예제 입력 3
# 4 10
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1
# 예제 출력 3
# 7


# 1차 시도 솔루션
def solution1(n, m, s):
    answer = 0
    ansarray = []
    for i in s:
        print(i)

        if len(ansarray) < 4:
            ansarray.append(max(i))
        else:
            if max(i) > min(ansarray):
                ansarray.append(max(i))
                ansarray.remove(min(ansarray))

    print(ansarray)
    answer = sum(ansarray)

    return answer


#2차 시도 솔루션

# 모든 방향이 경우를 구한다
directions = [[()]]

# 모든 점을 돌면서 합을 구하고

# 기존 최대값과 비교한다

def solution(n, m, s):
    maxTetrominoValue = 0
    print(*s)

    for rowIndex, rowValue in enumerate(s):
        for colIndex, colValue in enumerate(rowValue):
            
            
            maxTetrominoValue = max(maxTetrominoValue, colValue)
            print(rowIndex, colIndex, "value : ", colValue)

    return maxTetrominoValue


n = 4
m = 5
s = [[1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5]
     ]


print(solution(n, m, s))
