# https://school.programmers.co.kr/learn/courses/30/lessons/181896

# index가 O(N)이므로, 최악의 경우 맨마지막에 음수가 나오면 loop 2바퀴를 돕니다. enumerate(num_list): 이용하면 좋을 듯
def solution(num_list):
    for index, number in enumerate(num_list):
        if number < 0:
            return index
    return -1


if __name__ == '__main__':
    print(solution([12, 4, 15, 46, 38, -2, 15]))
