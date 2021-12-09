def solution(n,m):
    answer = []

    for number in range(1,n+1):
        for number2 in range(1,m+1):
            answer.append(number)

    return answer

if __name__ == '__main__':
    print(solution(4,2))
