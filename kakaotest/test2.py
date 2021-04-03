def solution(rows, columns, queries):
    answer = []
    matrix = []

    for i in range(1, rows + 1):
        temp = []
        for j in range(1, columns + 1):
            temp.append((i - 1) * columns + j)
        matrix.append(temp)

    for i in queries:
        # print("matrix ------- ", matrix)
        minlist = []
        tempmatrix = matrix.copy()
        # [
        # 0, 2
        # 1, 2
        # 2, 5
        # 3, 4
        # ]
        if abs(i[2] - i[0]) == abs(i[3] - i[1]):
            for j in range(i[0], i[2]):
                tempmatrix[i[0] - 1][j] = matrix[i[0] - 1][j - 1]
                minlist.append(tempmatrix[i[0] - 1][j])

            for j in range(i[0] - 1, i[2] - 1):
                tempmatrix[i[2] - 1][j] = matrix[i[2] - 1][j + 1]
                minlist.append(tempmatrix[i[2] - 1][j])

            for j in range(i[1], i[3]):
                tempmatrix[j][i[3] - 1] = matrix[j - 1][i[3] - 1]
                minlist.append(tempmatrix[j][i[3] - 1])

            for j in range(i[1] - 1, i[3] - 1):
                tempmatrix[j][i[1] - 1] = matrix[j + 1][i[1] - 1]
                minlist.append(tempmatrix[j][i[1] - 1])

        # elif abs(i[0] - i[2]) > abs(i[1] - i[3]):
        #     for j in range(i[1] - 1, i[3] - 1):
        #         tempmatrix[i[0] - 1][j] = matrix[i[0] - 1][j - 1]
        #         minlist.append(tempmatrix[i[0] - 1][j])
        #
        #     for j in range(i[1], i[3]):
        #         tempmatrix[i[2] - 1][j] = matrix[i[2] - 1][j + 1]
        #         minlist.append(tempmatrix[i[2] - 1][j])
        #
        #     for j in range(i[0] - 1, i[2] - 1):
        #         tempmatrix[j][i[3] - 1] = matrix[j - 1][i[3] - 1]
        #         minlist.append(tempmatrix[j][i[3] - 1])
        #
        #     for j in range(i[0], i[2]):
        #         tempmatrix[j][i[1] - 1] = matrix[j + 1][i[1] - 1]
        #         minlist.append(tempmatrix[j][i[1] - 1])

        else:
            for j in range(i[1], i[3]):
                tempmatrix[i[0] - 1][j] = matrix[i[0] - 1][j - 1]
                minlist.append(tempmatrix[i[0] - 1][j])

            for j in range(i[1] - 1, i[3] - 1):
                tempmatrix[i[2] - 1][j] = matrix[i[2] - 1][j + 1]
                minlist.append(tempmatrix[i[2] - 1][j])

            for j in range(i[0], i[2]):
                tempmatrix[j][i[3] - 1] = matrix[j - 1][i[3] - 1]
                minlist.append(tempmatrix[j][i[3] - 1])

            for j in range(i[0] - 1, i[2] - 1):
                tempmatrix[j][i[1] - 1] = matrix[j + 1][i[1] - 1]
                minlist.append(tempmatrix[j][i[1] - 1])
        # print(i, tempmatrix)
        answer.append(min(minlist))
        matrix = tempmatrix.copy()

    # print(matrix)
    return answer


rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]  # [8, 10, 25]
# 3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
# 100	97	[[1,1,100,97]]	[1]

print(solution(rows, columns, queries))
