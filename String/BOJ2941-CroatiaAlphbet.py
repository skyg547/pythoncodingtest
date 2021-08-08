# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳

# 문제를 잘못 이해
# 3개씩 가지고 와야 한다.
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
            for char in element:
                answerSet.add(char)
        cnt += 1
    print(len(answerSet))
