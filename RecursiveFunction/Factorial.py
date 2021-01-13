# 팩토리얼

def factorial_recursive(n):
    if n <= 1:
        return
    return n*factorial_recursive(n-1)

print('재귀 구현', factorial_recursive(5))