def solution(arr):
    arr = [2, 1, 3, 1, 2, 1]
    answer = []

    countArray = [0,0,0]

    for element in arr:
        if element == 1:
            countArray[0] += 1
        elif element == 2:
            countArray[1] += 1
        else:
            countArray[2] += 1


    for countNumber in countArray:
        answer.append(max(countArray) - countNumber)

    return answer


if __name__ == '__main__':
    solution([])