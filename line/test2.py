import re


def solution(sentences, n):
    # 1 점수계산
    # 대문자 포함 여부, 대문자의 문자수 계산
    checkUpper = re.compile('[A-Z]')
    scoreList = []

    # 문자 구성 개수 여부
    for sentence in sentences:
        alphabetSet = set()
        scoreDict = dict()
        upperCount = 0
        for alphabet in sentence.replace(' ', ''):
            if checkUpper.match(alphabet):
                upperCount += 1
            alphabetSet.add(alphabet.lower())
            # print(list(checkUpper.search(alphabet)))
        if upperCount > 0:
            alphabetSet.add('S')

        scoreDict['needKey'] = ''.join(sorted(alphabetSet))

        scoreDict['score'] = len(sentence) + upperCount
        scoreList.append(scoreDict)

    score = -1
    for scoreDict in scoreList:
        score2 = 0
        for scoreDict2 in scoreList:
            if scoreDict2['needKey'] in scoreDict['needKey']:
                score2 += scoreDict2['score']
        score = max(score2, score)

    return score


if __name__ == '__main__':
    print(solution(["line in line", "LINE", "in lion"], 5))
