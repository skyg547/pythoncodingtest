# https://www.acmicpc.net/problem/2866
# 문자열 잘라내기


# 1. 가장 위의 행을 지워도 테이블의 열을 읽어서 문자열이 중복되지 않는다면,
# 2. 가장 위의 행을 지워주고, count의 개수를 1 증가시키고

# 문제를 이해 못하겠슴
def solution(String):
    print(list(map(lambda x: str(x[0] + x[1]), zip(*String))))

    return


if __name__ == '__main__':
    R, C = 2, 6
    String = ['dobarz',
              'adatak']

    print(solution(String))
