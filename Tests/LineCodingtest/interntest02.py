def solution(l):
    answer = []

    for element in range(len(l)):

        breakT = 0

        # 가장 큰 원소면 -1
        if l[element] == max(l):
            answer.append(-1)
            continue

        if element == 0:
            if l[element + 1] > l[element]:
                answer.append(element + 1)
                continue
        elif element == len(l) - 1:
            if l[element - 1] > l[element]:
                answer.append(element - 1)
                continue

        for element2 in range(element, 0, -1):
            if l[element] < l[element2]:
                answer.append(element2)
                breakT = 1
                break
        if breakT == 1:
            continue
        for element2 in range(element, len(l)):
            if l[element] < l[element2]:
                answer.append(element2)

                break

    return answer


if __name__ == '__main__':
    l = [3, 5, 4, 1, 2]

    print(solution(l))
