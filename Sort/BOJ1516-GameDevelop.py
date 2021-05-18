# https://www.acmicpc.net/problem/1516
# 게임개발

def solution(lists):
    answer = []

    for i in lists:
        if len(i) == 2:
            answer.append(i[0])

        else:
            time = i[0]
            for j in range(1, len(i)):
                if i[j] == -1:
                    answer.append(time)
                else:
                    time += answer[i[j] - 1]
            # 중복 찾기
    return answer


if __name__ == '__main__':

    n = int(input())
    lists = [list(map(int, input().split())) for _ in range(n)]
    # print(lists)

    ans = solution(lists)
    for elemant in ans:
        print(elemant)
