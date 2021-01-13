#문자열 재정렬

data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    # 알 파벳인 경우 결과 리스트에 삽이
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

# 알파벳 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입

if value != 0:
    result.append(str(value))

print(''.join(result))


