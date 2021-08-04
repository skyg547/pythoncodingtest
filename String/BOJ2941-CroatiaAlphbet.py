# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳
import  re

if __name__ == '__main__':
    strings = input()

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
           cnt += 1

    print(cnt)