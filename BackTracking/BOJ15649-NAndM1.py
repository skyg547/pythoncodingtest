def solution(n, m):
    answer = []
    sets = set()
    for number in range(1, n + 1):
        for number2 in range(1, m + 1):
            answer.append(number)

    return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solution(n, m))
