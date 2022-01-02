<<<<<<< HEAD
def solution(x):
 sorted(x)

print(solution(input()))
=======
>>>>>>> a9f2226b0caf86bc64dde4d2a0e0e24de4f36904
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
