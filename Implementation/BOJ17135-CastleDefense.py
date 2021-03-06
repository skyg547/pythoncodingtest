# # https://www.acmicpc.net/problem/17135
# # 캐슬디펜스
#
#
# 조건 정리.
# 1. 격자판은 1×1 크기의 칸으로 나누어져 있고,
# 2. 각 칸에 포함된 적의 수는 최대 하나이다
# 3. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다
# 4. 궁수 3명을 배치, 성이 있는 칸에 배치, 하나의 칸에는 최대 1명의 궁수
# 5. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다.
# 6. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고,적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격
# 7. 같은 적이 여러 궁수에게 공격당할 수 있다
# 8. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.
# 9. 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
#
# 방안
# 1. 가장 많은칸 3곳 궁수 배치 -> 세로 탐색해서 세기 ---> 조합을 사용해서 모든 경우를 돌려놔야 한다.
# 2. 조건 구현
# 3. 공격 구현
# 4. 이동 구현
# 5. 궁수 배치
# 6.


def solution(d, l):


    return


if __name__ == '__main__':
    n, m, d = 5, 5, 1
    l = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]]
    print(*zip(*l))
    solution(d, l)
