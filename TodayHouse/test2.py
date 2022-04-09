from collections import defaultdict


# 말버릇 패턴이란 문자 데이터에서 가장 많이 등장하는
# 길이 1 이상의 패턴이며,
# 문자 데이터에 등장하는 해당 패턴을 모두 삭제하면 됩니다
# 가장 많이 등장한 것들을 추출
# 가장 많이 등장한 것들을 추출 후 길이 비교 밑 속하는지 비교
# 뽑고
# 정규표현식으로 제거
# upper case 처리

def solution(call):
    stringCollection = defaultdict(lambda: 0)
    Calls = call.lower()
    for first in range(len(Calls) + 1):
        for last in range(len(Calls) + 1):
            stringCollection[Calls[first:last]] += 1

    stringCollection[''] = 0
    manyWordCollection = []
    manyWord = sorted(stringCollection.items(), key=lambda x: (-x[1], -len(x[0])))
    maxValue = max(stringCollection.values())
    for strings in manyWord:
        if strings[1] == maxValue:
            manyWordCollection.append(strings[0])

    answer = call
    manyWordCollection.sort(reverse=True, key=lambda x: len(x))
    for strings2 in manyWordCollection:
        answer = answer.replace(strings2, '')

        answer = answer.replace(str(strings2).upper(), '')
    return answer


if __name__ == '__main__':
    print(solution("abcabcdefabc"))
