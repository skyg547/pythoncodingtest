# 처음과 끝이 이어져 있는 문자열을 상상

# 당신은 해당 문자열 내의 "같은 글자가 연속해 있는 구간 "
# 문자열 s 가 매개 변수로 주어짐 , s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬 return

# 3 ≤ s의 길이 ≤ 1,000
# s는 영어 소문자로 이루어진 문자열입니다.


#
# import re
#
# regex = re.compile("[a-z]+")
#
# print(regex.findall(s))


def solution(s):
    answer = []
    charCount = 1
    tempChar = ''

    for index, char in enumerate(s):
        if char == tempChar:
            charCount += 1
        else:
            answer.append(charCount)
            charCount = 1

        tempChar = char

        if index == len(s) - 1:
            if s[0] == s[-1]:
                answer[1] += charCount
            else:
                answer.append(charCount)

    return sorted(answer[1:])

if __name__ == '__main__':
    solution("wowwow")
