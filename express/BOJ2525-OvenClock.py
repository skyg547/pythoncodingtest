# https://www.acmicpc.net/problem/2525

if __name__ == '__main__':
    a, b, = map(int,input().split())
    c = int(input())

    a += (b + c) // 60

    print(a % 24, (b + c) % 60)
