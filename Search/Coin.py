# def solution(n, a, b, c, d):
#     # 총 개수에서 -
#     if n % 5 > a:
#         return [0, 0, 0, 0]
#     # 1 ,5 ,10 ,25
#
#     lists = []
#
#     # 모든 경우의수 사용
#     for i in reversed(range(a + 1)):
#         if n == i:
#             # lists.append([i, 0, 0, 0])
#             return [i, 0, 0, 0]
#
#         if n > 5:
#             for j in reversed(range(b + 1)):
#                 if n == i + 5 * j:
#                     # lists.append([i, j, 0, 0])
#                     return [i, j, 0, 0]
#                 if n > 10:
#                     for k in reversed(range(c + 1)):
#                         if n == i + 5 * j + 10 * k:
#                             # lists.append([i, j, k, 0])
#                             return [i, j, k, 0]
#                         if n > 25:
#                             for x in reversed(range(d + 1)):
#                                 if n == i + 5 * j + 10 * k + 25 * x:
#                                     lists.append([i, j, k, x])
#
#     print(lists)
#     max = 0
#
#     for i in lists:
#         if max < sum(i):
#             maxlist = i
#     # print(maxlist)
#
#     # return a - maxlist[0] , b - maxlist[1], c - maxlist[2], d-maxlist[3]
#
#     return maxlist

def solution(n, a, b, c, d):
    lists = []
    if n%5 > a:
        return [0,0,0,0]
    else:
        lists.append(n%5)
        n = n - n%5
        if n%10 > b*5:
            return [0,0,0,0]
        else:
            lists.append(n%10)
            n = n - n%10
            if n%25 > c*10:
                return [0,0,0,0]
            else:
                lists.append(n%25)
                n = n - n%25
                lists.append(n)

                return lists





n, a, b, c, d = 12, 5, 3, 1, 2

n, a, b, c, d = map(int, input().split())

print(*solution(n, a, b, c, d))
