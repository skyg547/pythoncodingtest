# https://www.acmicpc.net/problem/6588
# 골드 바흐의 추측
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
# 입력의 마지막 줄에는 0이 하나 주어진다.
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.
# 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또,
# 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.


import sys


# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 1배수들을 False 판정
                sieve[j] = False

    # 정해진 배열이 소수 여부 반환
    return sieve


primeList = prime_list(1000000)

while True:
    numbers = int(sys.stdin.readline())
    if numbers == 0:
        break

    isPrint = False
    for primeIndex in range(3, len(primeList)):  # 1은 소수가 아니고 2는 짝수라 3부터 시작
        if primeList[primeIndex] and primeList[numbers - primeIndex]:  # 2개다 소수 일 경우 출력
            print(str(numbers) + ' = ' + str(primeIndex) +
                  ' + ' + str(numbers - primeIndex))
            isPrint = True
            break

    if isPrint is False:
        print("Goldbach's conjecture is wrong.")
