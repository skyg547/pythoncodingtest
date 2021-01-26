# 타겟 넘버
# 문제 설명
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# 입출력 예 설명
# 문제에 나온 예와 같습니다.
#
# 구현 실패 오답

# from collections import deque
#
# answer = 0
#
#
# def solution(numbers, target):
#     queue = deque(numbers)
#     global answer
#     A(queue, target, 0, 0)
#
#     return answer
#
#
# def A(queue, target, now, b):
#     global answer
#     if (queue == None):
#         if now == target:
#             answer = + 1
#             return
#     queue.popleft()
#     now += b
#
#     A(queue, target, now, +queue[0])
#     A(queue, target, now, -queue[0])
#
#     return
#
#
# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target))

# 인터넷 해설
#
# global answer
# answer = 0
#
# def DFS(id, numbers, target, value):
#     global answer
#
#     if id == len(numbers):
#         if target == value:
#             answer += 1
#             return
#         else:
#             return
#
#     DFS(id + 1, numbers, target, value + numbers[id])
#     DFS(id + 1, numbers, target, value - numbers[id])
#
#
# def solution(numbers, target):
#     global answer
#
#     DFS(0, numbers, target, 0)
#     return answer


# 모법답안
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:  # 재귀를 돌면서 리턴값 더하기
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


#모범답안2

from itertools import product


def solution(numbers, target):
    # 리스트에 +,- 쪼개서 넣어버리기
    l = [(x, -x) for x in numbers]
    print(l)
    # 프로덕트 함수,
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    print(s)
    # 카운트 함수
    return s.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
