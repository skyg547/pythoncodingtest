def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 함수에서 ',i+1,'재귀함수를 호출 합니다.')
    recursive_function(i+1)
    print(i,'재귀 함수를 종료 합니다')

recursive_function(0)