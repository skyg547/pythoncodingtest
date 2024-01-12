# https://school.programmers.co.kr/learn/courses/30/lessons/181940?language=python3

def solution(my_string, k):
    answer = ''
    for _ in range(k):
        answer += my_string
    return answer


if __name__ == '__main__':
    print(solution('23', 2));
