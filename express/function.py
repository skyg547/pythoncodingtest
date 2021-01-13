def add(a,b):
    return a + b
print(add(3,7))

def add(a,b):
    print('함수의 결과:', a + b)

add(a  = 8, b = 2)

a = 0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

array = [1,2,3,4,5]

def func():
    global array
    array = [3,4,5]
    array.append(6)
    print(array)

func()
print(array)

def operator(a,b):
    add_var = a+b
    subtract_var = a*b
    multiply_var = a*b
    divide_var = a/b
    return add_var, subtract_var, multiply_var, divide_var

a,b,c,d = operator(7,3)
print(a,b,c,d)