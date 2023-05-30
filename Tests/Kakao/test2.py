# 하죄상우
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def find(map):
    for row in range(len(map)):
        for element in range(len(map[row])):
            # 먼 p 인지 아닌지 탐색 Place를 돌면서
            if map[row][element] == 'P':
                # 사방탐색 벅 벽을 벗어 나면 안댄다
                for index in range(4):
                    # 벗어나면 위반
                    if not (0 <= row + dx[index] < len(map)) or not (0 <= element + dy[index] < len(map[row])):
                        break
                    # 사방 탐색 진행 p 면 위반
                    elif map[row + dx[index]][element + dy[index]] == 'P':
                        return 0
                    # o 면 또 사방탐색
                    elif map[row + dx[index]][element + dy[index]] == 'O':
                        # 2번째 사방 탐색 시작
                        for index2 in range(4):
                            # 벗어나면 위반
                            if not (0 <= row + dx[index] + dx[index2] < len(map)) or not (
                                    0 <= element + dy[index] + dy[index2] < len(map[row])):
                                break
                            # 그전 위치로 돌아 올면 하지말자
                            elif (row + dx[index] + dx[index2]) == (row) and (element + dy[index] + dy[index2]) == (
                                    element):
                                break
                            # 사방 탐색 해서 P 면 위반
                            elif map[row + dx[index] + dx[index2]][element + dy[index] + dy[index2]] == 'P':
                                return 0

                    # 일단 동서남북탐색 o 이면 들어가서 또 탐색 동서남북 한다 , p 가 나올경우 바로 return 1 .
                    # 거기서  o 이면 양옆 탐색 인데 p 가오면 거리 규칙 어김

    return 1


# dfs 문제
def solution(places):
    answer = []

    # | r1 - r2 | + | c1 - c2 |

    for place in places:
        answer.append(find(place))

    # print(places)
    return answer


if __name__ == '__main__':
    place = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ["OOOOP", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]
    ]

    print(solution(place))
