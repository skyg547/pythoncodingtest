# https://www.acmicpc.net/problem/12852
# 1로 만들기 버전 2

import sys


#dp로 만들어서 해결하기


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
    ans = [0]*(10**6+1)

    # 초기 3갯값 설정
    ans[1] , ans[2], ans[3] = 1, 1, 1

    # 1,2,3이면 1 반환
    if 0 < n < 4:
        return 1

    # 4 부터 돌기 시작
    for index in range(4, n+1):
        # ans의 값은 3개 중 가장 작은거
        ans[index] = min(ans[index-1], ans[index//3], ans[index//2])+1

        # 각 연산을 한번씩 해봐야함 ?

        # 1
    return ans[n]
    print(ans)





if __name__ == '__main__':
    print(solution(10))

# 3
# 10  9 3 1
