#빼거나 나누기 문제
n, k = map(int, input().split())

print(n, k)

result = 0

while True:
    # n을 k 로 나눌수 있는 수로 1을 빼서 만들기
    # target = 나눌수 있는 수
    target = (n//k)*k
    # result 에 -1 한 횟수를 더해주기
    result += (n-target)
    n = target

    if n < k:
        break;

    result += 1
    n //= k

result += (n-1)

print(result, n)