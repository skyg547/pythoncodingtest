# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳

# 문제를 잘못 이해
# 3개씩 가지고 와야 한다.
# 문제 잘못 이해 크로아티아 알파벳도 하나에서 총 몇개의 알파벳이냐 !
import re

if __name__ == '__main__':
    strings = input()

    answerSet = set()

    s = ["c=",
         "c-",
         "dz=",
         "d-",
         "lj",
         "nj",
         "s=",
         "z="]

    cnt = 0
    for element in s:
        if re.compile(element).search(strings) != None:
            strings = strings.replace(element, '0')

    print(len(strings))