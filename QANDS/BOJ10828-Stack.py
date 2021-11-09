#push X: 정수 X를 스택에 넣는 연산이다.pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.size: 스택에 들어있는 정수의 개수를 출력한다.empty: 스택이 비어있으면 1, 아니면 0을 출력한다.top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다

def solution(arr): 
  stack = []

  for command in arr: 
    commands = command.split()

    if commands[0] == 'push' :
      stack.append(commands[1])
    elif commands[0] == 'size': 
      print(len(stack))
    elif command[0] == 'pop' :
      print(stack.pop())
    elif command[0] == 'top' :
      print(stack[-1])
    elif command[0] == 'empty' :
      if len(stack) == 0 :  
        print(1)
      else :
        print(0)
      
i = input()

arr = [input() for _ in range(i)]
solution(arr)