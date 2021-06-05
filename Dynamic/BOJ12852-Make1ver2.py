# https://www.acmicpc.net/problem/12852
# 1로 만들기 버전 2
import copy
import sys


# dp로 만들어서 해결하기


#
# def solution(n):
#     answer1 = 1e9
#     answer2 = [0]
#     cnt = 0
#
#     while n != 1:
#         cnt += 1
#         if n % 3 == 0:
#             n //= 3
#         elif n % 2 == 0:
#             n //= 2
#         else:
#             n -= 1
#
#     # 1일때 그전 결과 값이랑 비교
#     if n == 1:
#         answer1 = min(answer1, cnt)
#         return answer1

def solution(n):
    answer = [100000000] * (10 ** 6 + 1) # 그냥배열
    answer2 = [[1]] * (10 ** 6 + 1) # 경로배열
    answer3 = []
    # 초기 3갯값 설정
    answer[1], answer[2], answer[3] = 1, 1, 1
    answer2[2], answer2[3] = [1, 2], [1, 3]
    # 1,2,3이면 1 반환
    if 0 < n < 4:
        return answer[n], answer2[n]

    # 1부터 돌기
    for index in range(1, n):
        # 지금 꺼에 1을 더한게 더 작다면 ?
        if answer[index] + 1 < answer[index + 1]:
            answer[index + 1] = answer[index] + 1 # 작은값으로 대체
            answer2[index + 1] = copy.deepcopy(answer2[index]) # 경로도 대체
            answer2[index + 1].append(index + 1) # 그 값 더해주기
            answer3.append(index)
        # 만약 3을 곱했을 때 n을 넘기지 않는다면
        if index <= (n // 3):
            if answer[index] + 1 < answer[index * 3]:
                answer[index * 3] = answer[index] + 1
                answer2[index * 3] = copy.deepcopy(answer2[index])
                answer2[index * 3].append(index * 3)
                answer3.append(index)
        # 만약 2를 곱했을 때 n을 넘기지 않는다면
        if index <= (n // 2):
            if answer[index] + 1 < answer[(index * 2)]:
                answer[index * 2] = answer[index] + 1
                answer2[index * 2] = copy.deepcopy(answer2[index])
                answer2[index * 2].append(index * 2)
                answer3.append(index)
    print(answer3)
    return answer[n], answer2[n]


if __name__ == '__main__':
    answer = (solution(int(sys.stdin.readline())))

    print(answer[0])
    print(*answer[1][::-1])
# 3
# 10  9 3 1
