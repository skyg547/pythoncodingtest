# # https://www.acmicpc.net/problem/9935
# # 문자열 폭발
#
# # 45% 메모리 초과
# def Boom(l, s):
#     newl = ''
#     newl = l.replace(s, '')
#
#     if s in newl:
#         t = Boom(newl, s)
#         newl = t
#         return t
#
#     return newl
#
#
# def solution(l, s):
#     t = Boom(l, s)
#     if t == '':
#         return 'FRULA'
#     else:
#         return t
#
# if __name__ == '__main__':
#     l = 'mirkovC4nizCC44'
#     s = 'C4'
#     l = input()
#     s = input()
#     print(solution(l, s))


# string = list(map(str, input()))
# bomb = list(map(str, input()))

string = 'mirkovC4nizCC44'
bomb = 'C4'
string = list(map(str, input()))
bomb = list(map(str, input()))

length = len(bomb)

#  문자 ,인덱스, 인덱스
mem = [[-1, -1, -1]]  # 폭탄일 수도 있는 단어저장,그 단어의 인덱스 저장, 그단어의 폭탄 인덱스 저장,
bomb_idx = 0

for i in range(len(string)):
    s = string[i]
    if s not in bomb:
        mem = [[-1, -1, -1]]
        bomb_idx = 0
        continue
    if s == bomb[bomb_idx]:
        # 단어오 인덱스 그 폭탄 저장 해주고
        mem.append([s, i, bomb_idx])
        # print(mem)
        # 붐 인덱스 증가
        bomb_idx += 1
        # 붐 인덱스 랑 길이 비교
        if bomb_idx == length:
            for upo in range(length):
                g, e, l = mem.pop()
                string[e] = ""
            bomb_idx = mem[-1][-1] + 1
            # print(">>>>>>>> ", *string, sep="")
    #만약 지금 현재 문자열이 첫번째 와 같다면
    elif s == bomb[0]:
        mem.append([s, i, 0])
        # print(mem)
        bomb_idx = 1
    # print(mem, "index =", bomb_idx)

ans = "".join(string).rstrip()
print(ans if ans else "FRULA")
