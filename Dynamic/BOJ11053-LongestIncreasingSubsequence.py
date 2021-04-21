# 가장 긴 증가하는 부분 수열
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	71114	27341	18053	36.870%
# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

def solution(a, l):
    # 메모제이션을 다 실시
    answer = [1] * len(l)

    #
    # 반례 2 때문에 해결이 안댐
    # # 정답 배열의 길이 만큼 돌기
    # for i in range(len(answer)):
    #     # 임시 배열 생성
    #     templist = []
    #     # 배열에 현재 위치 넣기
    #     templist.append(l[i])
    #
    #     # 자기보다 뒤에 배열을 돌면서
    #     for j in range(i, len(l)):
    #         # 만약에 현재 배열의 넣어진 최신 값보다 크면
    #         if templist[-1] < l[j]:
    #             # 배열에 값 추가
    #             templist.append(l[j])
    #     # print(templist)
    #     answer[i] = len(templist)

    # 길이 만큼 도는데
    # LIS 알고리즘
    # answer 배열을 돌면서
    for i in range(1, len(l)):
        # 자기 인덱스 직전값 까지 돌면서
        for j in range(0, i):

            # 만약 자기 보다 작은 값이 있으면?
            if l[i] > l[j]:
                # 작은값 +1 하거나 , 자기 값 저장
                answer[i] = max(answer[i], answer[j] + 1)
    # print(answer)
    return max(answer)


if __name__ == '__main__':
    A = 6
    aList = [10, 20, 10, 30, 20, 50]

    # 반례 - 첫번째
    # 20 10 30 20 50

    # 7 반례 두번쨰
    # 1 4 5 2 3 4 5

    A = int(input())
    aList = list(map(int, input().split()))

    print(solution(A, aList))
