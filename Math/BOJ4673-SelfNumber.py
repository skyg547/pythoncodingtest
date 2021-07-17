# # https://www.acmicpc.net/problem/4673
# # 셀프 넘버
#

def solution():
    return


if __name__ == '__main__':

    result = []
    for index in range(9994):
        result.append(index)

    for x in range(10001):

        y = x
        # # print("초기 x =", x)
        # y += (x % 10)  # 1의 자리수 제거
        # y += ((x % 100) // 10)  # 10의 자리수
        # y += ((x % 1000) // 100)  # 100의 자리수
        # y += ((x % 10000) // 1000)  # 1000의 자리수
        stringX = str(x)
        for element in stringX:
            y += int(element)

        if y > 10000:
            break
        if y in result:
            result.remove(int(y))

    for element in result:
        print(element)
