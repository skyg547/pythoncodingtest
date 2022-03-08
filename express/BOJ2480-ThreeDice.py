# acmicpc.net/problem/2480
from collections import Counter

if __name__ == '__main__':

    m = list(map(int,input().split()))
    count = sorted(Counter(m), reverse = True)
    if (len(count) == len(m)):
        print(max(count)*100)
    elif len(count) == 1:
        print(count.pop()*1000+10000)
    else:
        print(count.pop() * 100 + 1000)