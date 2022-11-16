# https://www.acmicpc.net/problem/18290
# N과M k

directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}

if __name__ == '__main__':
    rowNumber, colNumber, selectCount = map(int, input().split())
    numberMatrix = [list(map(int, input().split())) for _ in range(rowNumber)]

    for rowindex, row in enumerate(numberMatrix):
        for colindex, col in enumerate(row):
            for selectrowindex, row in range(rowindex, rowNumber+1 ):
                for colindex, col in range(colindex, colNumber+1 ):
                    for direction in directions:

                    print(rowindex, colindex)
                    print(row,col)
