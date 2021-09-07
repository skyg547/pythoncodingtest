# https://www.acmicpc.net/problem/10250
# ACM 호텔

def solution():
    return

if __name__ == '__main__':

    for _ in range(int(input())):
        a , b , c = map(int, input().split())
        print(str(c%a+1)+str(c%a+1).zfill(max(2,len(str(c)))))

