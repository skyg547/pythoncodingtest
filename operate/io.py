import sys
#한줄의 문자열을 입력 받는 함수 input
#리스트의 모든 원소에 각각 특정한 함수를 적용할 때 map()

n = int(input())
print(n)

data = list(map(int, input().split()))
print(data)

#언팩킹                팩킹             공백을 기준으로 구분하여 입력
a, b, c = map(int, input().split())
print(a,b,c)

#빠르게 입력받기

data = sys.stdin.readline().rstrip()
print(data)


a=1
b=2
print(a,b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은" + str(answer) + "입니다.")

answer = 7
print(f"정답은 {answer} 입니다.")