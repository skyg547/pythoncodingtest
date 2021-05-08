def solution(n, k, cmd):
    answer = ['0'] * n

    tmpRemove = 0
    index = k

    for command in cmd:
        # 위 선택
        if command[0] == "U":
            index -= int(command[2])

        # 아래선택
        elif command[0] == "D":
            index += int(command[2])

        # 삭제 후 아래선택 but 마지막 행이면 바로 윗행 선택
        elif command[0] == "C":
            if "X" in answer:
                if (n - 1 - answer[::-1].index("X")) == index:
                    tmpRemove = index
                    answer[index] = "X"
                    index -= 1
                    continue

            tmpRemove = index
            answer[index] = "X"
            index += 1
        # print(answer[::-1])
        # tmpRemove = index
        # 삭제 복구
        elif command[0] == "Z":
            answer[tmpRemove] = "O"

    return answer


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    "OOXOXOOO"
    print(solution(n, k, cmd))
