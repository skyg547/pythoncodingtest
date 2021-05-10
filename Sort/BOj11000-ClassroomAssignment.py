# 강의실 배정
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	9190	2723	1922	28.989%
# 문제
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
#
# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
#
# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
#
# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!
#
# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
#
# 이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)
#
# 출력
# 강의실의 개수를 출력하라.
#
# 예제 입력 1
# 3
# 1 3
# 2 4
# 3 5
# 예제 출력 1
# 2

import heapq, sys


def solution(l):

    # 가장 작은 시작값부터 넣어 주는데, 같으면 끝나는 시간이 작은걸 넣어 준다.
    l.sort(key= lambda x: (x[0],(x[1])))
    # 큐를 만들고
    qoduf = []
    # 배열만큼 도는데
    for element in l:
        # 만약 배열이 비어있지 않고, 배열이 끝값보다, 돌려는 수이 값과 같거나 작다면
        if qoduf and qoduf[0] <= element[0]:
            heapq.heappop(qoduf) # 빼주고
        heapq.heappush(qoduf, element[1]) # 교체해주거나, 넣어준다a, 끝값을
    print(len(qoduf)) # 최종적으로 배열이 길이가 강의실의 수이므로 호출해 주면 된다
    return

# input -> 시간 초과

if __name__ == '__main__':


    n= int(sys.stdin.readline())
    l = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    solution(l)
