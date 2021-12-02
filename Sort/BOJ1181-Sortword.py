# https://www.acmicpc.net/problem/1181

def solution(x):
    return sorted(x, key=lambda x: (len(x), x))


number = int(input())
wordList = [input() for _ in range(number)]

for word in solution(set(wordList)):
    print(word)

# print(*solution(wordList))
#
# print(solution(['but',
#                 'i',
#                 'wont',
#                 'hesitate',
#                 'no',
#                 'more',
#                 'no',
#                 'more',
#                 'it',
#                 'cannot',
#                 'wait',
#                 'im',
#                 'yours']))
