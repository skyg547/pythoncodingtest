# https://www.acmicpc.net/problem/10809
# 알파벳 찾기
import string


def solution(strings):

    answer = '' # 조인할 문자열

    alpabat = dict() # 딕셔너리 선언

    # 입력받은거 돌면서
    for index, element in enumerate(strings):
        alpabat.setdefault(element, index) #엘리먼트 값으로 인덱스저장

    for element in string.ascii_lowercase: # string.ascil_lowercase => 소문자 알파벳 배열
        if element in alpabat: # 딕셔너리 안에 있으면
            answer += (str(alpabat[element])) #알파벳 더하기
        else:
            answer += (str(-1)) #-1  더하기
        answer += ' ' # 한칸 뛰어주고
    return answer

if __name__ == '__main__':

    print(solution(input()))