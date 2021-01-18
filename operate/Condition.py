#조건문
x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")

score = 95

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다')

else:
    print('성적이 70 점 미만입니다.')
    print('조금 더 분별 하세요')

print('프로그램을 종료합니다')
a = -20

if a >= 0:
    print("a>= 0")
elif a >= -10:
    print("0>a>= -10")

else:
    print("-10> a")

score = 85
if score >= 90:
    print("학점3점")
elif score >= 80:
    print("학점2점")
elif score >= 70:
    print("학점1점")
else:
    print("학점0점")

if not False:
    print("Yes")

a = 15
if a <= 20 and a >= 0:
    print("Yes")

# in, not in, pass 키워드

a = 50
if a >= 30:
    pass
else:
    print("a < 30")

score = 85
if score >= 80: result = "Success"
else: result = "Fail"

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

#대수학 부등식 사용가능
x=15

if 0<x<20:
    print("x는 0이상 20미만의 수입니다.")

