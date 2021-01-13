#곱하거나 더하기 문제
data = input()

result = int(data[0])

# 0,1이면 더하기 아니면 곱하기 인덱스로 접근
for i in range(1, len(data)):
    n = int(data[i])
    if n < 2 or result < 2:
        result += n
    else:
        result *= n

print(result)