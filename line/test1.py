import re
def solution(logs):
    logList = list()
    checkKey = ['team_name', 'application_name', 'error_level', 'message']
    checkValue = re.compile('.*[^a-zA-Z]+.*')

    for log in logs:
        # 길이100 체크
        if len(log) >= 100:
            continue
        # Key Value 묶어주기
        log = log.replace(' : ', '=')
        # key 갯수 검사, 값 영대소문자 검사
        if log.count(' ') != 3 or checkValue.match(log.replace('_', '').replace(' ', '').replace('=', '')):
            continue

        # 각 로그를 저장할 맵
        tempMap = dict()
        #  로그 키,값을 순회
        for logValue in log.split(' '):
            # 키 값 리스트
            logKeyAndValue = logValue.split('=')
            #  키값 찾아 주기
            for key in checkKey:
                # 키값이 있을시 맵에 넣어주기
                if logKeyAndValue[0] == key:
                    tempMap[logKeyAndValue[0]] = logKeyAndValue[1]

        # 모든 키가 들었는지 확인
        if len(tempMap) == 4:
            # print(tempMap)
            # 로그 수집
            logList.append(tempMap)
    return len(logs) - len(logList)


if __name__ == '__main__':
    print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
                    "no such file or directory",
                    "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11",
                    "team_name : recommend application_name : recommend error_level : info message : Success!",
                    "   team_name : db application_name : dbtest error_level : info message : test",
                    "team_name     : db application_name : dbtest error_level : info message : test",
                    "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))
