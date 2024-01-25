# https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    for number in num_list:
        if number < 0:
            return num_list.index(number)

    return -1


if __name__ == '__main__':
    print(solution([13, 22, 53, 24, 15, 6]))
