import itertools


def solution(dist):
    answer = []
    # 모든 경로 탐색
    for route in list(itertools.permutations(range(len(dist)), len(dist))):
        sumdistancce = 0
        previousNode = -1
        outflag = False

        for node in route:
            #  거리 더 해주기
            if previousNode != -1:
                sumdistancce += dist[node][previousNode]

            #  알맞느 거리인지 측정해준다.
            checkDistance = 0
            for checkNode in route:
                #  자기 자신일 경우 체크 할 필요 없음
                if checkNode == node:
                    break
                #  필요거리 보다, 현재 온 거리가 작다면 거짓
                if dist[checkNode][node] < sumdistancce - checkDistance:
                    outflag = True
                    break
                checkDistance += dist[checkNode][node]

            # 이전 노드 설정 해주기
            if outflag:
                break
            previousNode = node

        #  측정하면 답 배열에 담는다
        if not outflag:
            answer.append(list(route))
    return answer


if __name__ == '__main__':
    print(solution([[0, 5, 2, 4, 1], [5, 0, 3, 9, 6], [2, 3, 0, 6, 3], [4, 9, 6, 0, 3], [1, 6, 3, 3, 0]]))


#  시간초과

#  다른 풀이 필요