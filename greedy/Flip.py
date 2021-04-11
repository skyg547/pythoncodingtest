# 뒤집기
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	6883	3494	2744	51.099%
# 문제
# 다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
#
# 예를 들어 S=0001100 일 때,
#
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
#
# 문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.
#
# 입력
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다.
#
# 출력
# 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.


def solution(n):
    ans = 0
    onecnt1 = 0
    zerocnt1 = 0

    onecnt2 = 0
    zerocnt2 = 0
    for i in range(len(n)):

        # 마지막꺼 인지 아닌지
        if i == len(n) - 1:
            # 그 전꺼랑 비교 다르면 더하기
            if n[i - 1] != n[i]:
                # 0인지 1인지 체크
                if n[i] == '0':
                    zerocnt1 += 1
                else:
                    onecnt1 += 1
        # 일반 적 상황
        else:
            # 다음꺼랑 비교 다르면 더하기
            if n[i + 1] != n[i]:
                if n[i] == '0':
                    zerocnt1 += 1
                else:
                    onecnt1 += 1
    # print(onecnt1, zerocnt1)

    #역순 처리
    n = list(reversed(n))
    # print(n)
    for i in range(len(n)):

        # 마지막꺼 인지 아닌지
        if i == len(n) - 1:
            # 그 전꺼랑 비교 다르면 더하기
            if n[i - 1] != n[i]:
                # 0인지 1인지 체크
                if n[i] == '0':
                    zerocnt2 += 1
                else:
                    onecnt2 += 1
        # 일반 적 상황
        else:
            # 다음꺼랑 비교 다르면 더하기
            if n[i + 1] != n[i]:
                if n[i] == '0':
                    zerocnt2 += 1
                else:
                    onecnt2 += 1
    # print(onecnt2, zerocnt2)
    onecnt = max(onecnt2, onecnt1)
    zerocnt = max(zerocnt1, zerocnt2)

    # 예외처리 00001111
    if onecnt + zerocnt == 1:
        return 1
    # 둘중에 작은거 출력
    return min(onecnt, zerocnt)


if __name__ == '__main__':
    n = '0001100'
    # 테스트 케이스 실행결과
    # 첫번째 풀이에선 101100 2 1 로 집계되어
    # 역순 시켜준뒤 큰거로 가져옴
    # 그리고 다시 로직 처리

    n = input()
    print(solution(n))
