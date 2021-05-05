def solution(inputString):
    if inputString[0] in ']})>':
        return 0

    answer = 0
    stack = []

    for i in range(len(inputString)):
        if inputString[i] in '[({<':
            stack.append(inputString[i])
            answer += 1

        if inputString[i] in ']})>':
            if not stack:
                return -i

            if inputString[i] == ']':
                if stack[-1] != '[':

                    return -i
                else:
                    stack.pop()

            if inputString[i] == ')':
                if stack[-1] != '(':

                    return - i
                else:
                    stack.pop()

            if inputString[i] == '}':
                if stack[-1] != '{':
                    return -i

                else:
                    stack.pop()

            if inputString[i] == '>':
                if stack[-1] != '<':
                    return -i

                else:
                    stack.pop()

    if stack:
        return -(len(inputString) - 1)

    return answer


if __name__ == '__main__':
    l = 'line [({<plus>)}]'
    s = 'line[({<plus>}) - 15'
    d = '>_<'
    print(solution(l))
