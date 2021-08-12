# https://www.acmicpc.net/problem/1316
# 그룹단어체키

def solution(word):
    answer = 0
    # for element in word:
    #     if element i

    answerSet = set()
    temp = ""
    word = "abab"

    for element in word:
        answerSet.add(element)
        answerSet.add(temp)


    # 나온적 있으면 set 추가
    # 모든 나온걸 set 에 추가 하고 검사하자
    # 들어있느지 안들어 있는지
    return answer

if __name__ == '__main__':

    loop = int(input())
    count = 0

    for _ in range(loop):
        count += solution(input())

    print(count)