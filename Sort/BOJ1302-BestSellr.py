# 베스트 셀러
# 문제
# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
#
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
#
# 예제 입력 1
# 5
# top
# top
# top
# top
# kimtop
# 예제 출력 1
# top


def solution(l):
    # 딕셔너리를 만들어주고
    dicts = {}
    # 빌트인 이름 같지 않게조심하자

    # 받은 리스트를 돌면
    for i in l:
        # 딕셔너리에 있으면 1을 더해주고
        if i in dicts:
            dicts[i] += 1
        # 딕셔너리에 없으면 1로 만들어 준다
        else:
            dicts[i] = 1
    # 최대값을 저장해주고
    maxvalue = max(dicts.values())
    # 최대값인  책 배열을 만들어 주고
    answersheet = []

    #  딕셔너리 아이템을 돌면서
    for i, n in dicts.items():
        # 벨류가 최대값이면
        if n == maxvalue:
            # 리스트에 넣어주고
            answersheet.append(i)

    # 정렬을 해준다
    answersheet.sort()
    # print(answersheet)
    # 그리고 출력
    print(answersheet[0])
    # a = list(dict.items())
    # a.sort(key=lambda x: ((x[1]), (x[0][0])) )
    # # print(a)
    # print(a[1][0])
    # return max(dict.keys())


if __name__ == '__main__':
    n = 5
    l = [
        "top",
        "top",
        "top",
        "top",
        "kimtop",
        'zp'
    ]

    n = int(input())
    l = [input() for _ in range(n)]
    solution(l)

# # 반례 1
# 10
# dc
# zxo
# abd
# pa
# ccc
# dc
# sad
# zxcvdq
# qteq
# abd
