# 일단 varialbes 부터 비교해서 다 변환 해준다
# 일단 문제를 가려 내야 한다  --> 나중 철 ㅣ
# --> 무한 반복인지 아닌지 가려 낸다
from hash.BestAlbum import album


def solution(tstring, variables):
    answer = tstring
    isInfinite = True
    keyGroup = []

    # 키 그룹 설정
    for values in variables:
        keyGroup.append(values[0])

    # 값 부터 변환
    for valueIndex, values in enumerate(variables):
        # 바꾸는 변수인지 체크
        if values[1][0] == '{':
            for keys in variables:
                # slice or replace ?
                # 바꿔주기
                if str(values[1]).replace('{', '').replace('}', '') == keys[0] and keys[0] != values[0]:
                    variables[valueIndex][1] = keys[1]

        if str(values[1]).replace('{', '').replace('}', '') not in keyGroup:
            print(values[1], keyGroup)
            isInfinite = False

    # 무한 반복인지 체크
    if isInfinite:
        return tstring

    # 그대로 출력

    # 바꿔주고 출력 해주기
    # 문자를 가져오기
    word = ''
    isSaveWord = False
    for alphabet in tstring:
        if alphabet == '{':
            isSaveWord = True
            continue
        elif alphabet == '}':
            isSaveWord = False
            # 바꿔 준다
            for keyWord in variables:
                if keyWord[0] == word:
                    answer = answer.replace('{' + keyWord[0] + '}', keyWord[1])
            # word 초기화
            word = ''
        if isSaveWord:
            word += alphabet
    return answer


if __name__ == '__main__':
    print(solution("{a} {b} {c} {d} {i}", [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))
