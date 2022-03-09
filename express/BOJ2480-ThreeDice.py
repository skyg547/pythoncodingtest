# acmicpc.net/problem/2480
from collections import Counter

if __name__ == '__main__':

    m = list(map(int, input().split()))
    count = sorted(list(Counter(m).most_common()), reverse=True, key=lambda x: x[1])
    if len(count) == len(m):

        print(max(count, key=lambda x: x[0])[0] * 100)
    elif len(count) == 1:
        print(count[0][0] * 1000 + 10000)
    else:
        print(count[0][0] * 100 + 1000)
