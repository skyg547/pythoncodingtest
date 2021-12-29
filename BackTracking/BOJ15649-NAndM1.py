def solution(n, m):
    answer = []
    sets = set()
    for number in range(1, n + 1):
        for number2 in range(1, m + 1):
            answer.append(number)

    return answer


# make permutation
def permute(arr):
    result = [arr[:]]
    print(result)
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        print(i)
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else :
            c[i] = 0
            i += 1
    return result


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # print(solution(n, m))
    permute(['A', 'B' , 'C'])
