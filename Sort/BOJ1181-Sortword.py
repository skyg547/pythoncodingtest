# https://www.acmicpc.net/problem/1181

def solution(x):
    return sorted(x, key= lambda x : (len(x), x))


print(solution(['but',
                'i',
                'wont',
                'hesitate',
                'no',
                'more',
                'no',
                'more',
                'it',
                'cannot',
                'wait',
                'im',
                'yours']))
