# 문제 설명
# 안내
# 이 강의에서는 파이썬의 기초 문법을 다루지 않습니다. 이 강의는 파이썬 문법을 이미 알고 있는 분들을 위해서 만들었어요. 본 문제를 풀지 못하는 분은 프로그래머스의 파이썬 입문 강의 또는 김왼손의 미운코딩새끼 강의로 파이썬 기초를 다진 후 다시 와주세요.
#
# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.
#
# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist 각 원소의 길이는 100 이하인 자연수입니다.
# 예시
# input	output
# [[1], [2]]	[1,1]
# [[1, 2], [3, 4], [5]]

mylist = [[1], [2]]


def solution(mylist):
    # answer = []
    #
    # for x in mylist:
    #     answer.append(len(x))
    #
    # return answer --> c++ 형식
    return list(map(len,mylist))



print(len(mylist[0]))
print(solution(mylist))
