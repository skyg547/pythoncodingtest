# # def solution(n, a, b, c, d):
# #     # 총 개수에서 -
# #     if n % 5 > a:
# #         return [0, 0, 0, 0]
# #     # 1 ,5 ,10 ,25
# #
# #     lists = []
# #
# #     # 모든 경우의수 사용
# #     for i in reversed(range(a + 1)):
# #         if n == i:
# #             # lists.append([i, 0, 0, 0])
# #             return [i, 0, 0, 0]
# #
# #         if n > 5:
# #             for j in reversed(range(b + 1)):
# #                 if n == i + 5 * j:
# #                     # lists.append([i, j, 0, 0])
# #                     return [i, j, 0, 0]
# #                 if n > 10:
# #                     for k in reversed(range(c + 1)):
# #                         if n == i + 5 * j + 10 * k:
# #                             # lists.append([i, j, k, 0])
# #                             return [i, j, k, 0]
# #                         if n > 25:
# #                             for x in reversed(range(d + 1)):
# #                                 if n == i + 5 * j + 10 * k + 25 * x:
# #                                     lists.append([i, j, k, x])
# #
# #     print(lists)
# #     max = 0
# #
# #     for i in lists:
# #         if max < sum(i):
# #             maxlist = i
# #     # print(maxlist)
# #
# #     # return a - maxlist[0] , b - maxlist[1], c - maxlist[2], d-maxlist[3]
# #
# #     return maxlist
#
# # def solution(n, a, b, c, d):
# #     lists = []
# #     if n%5 > a:
# #         return [0,0,0,0]
# #     else:
# #         lists.append(n%5)
# #         n = n - n%5
# #         if n%10 > b*5:
# #             return [0,0,0,0]
# #         else:
# #             lists.append(n%10)
# #             n = n - n%10
# #             if n%25 > c*10:
# #                 return [0,0,0,0]
# #             else:
# #                 lists.append(n%25)
# #                 n = n - n%25
# #                 lists.append(n)
# #
# #                 return lists
#
#
# #
# # n, a, b, c, d = 12, 5, 3, 1, 2
# #
# # n, a, b, c, d = map(int, input().split())
# #
# # print(*solution(n, a, b, c, d))
# #
#
# 동전 해답 판

# X : 입력값(목표 금액)
# coin : 1, 5, 10, 25 센트 동전 갯수 (입력값)
# ans : X원 일때 최대 사용한 1, 5, 10, 25 센트 동전 갯수
# check : check[i] = x  i원을 만들기 위해 최대로 사용한 동전의 갯수 x개
# used : 특정 money원을 만들기 위해 사용한 1, 5, 10, 25 센트 동전의 갯수
# x : X원을 만들기 위해 필요한 최소 1센트 갯수

import sys

# 재귀가 많아 런타임에러 나기에 설정
sys.setrecursionlimit(10 ** 9)


# dfs로 가능한 경우를 모두 해봐야한다.

# dfs(money, cnt) : 가능한 모든 경우를 확인해보기 위한 재귀 함수
# moeny : 현재까지 동전의 합, cnt : 현재까지 동전의 갯수
def dfs(money, cnt):
    # 동전을 최대한으로 사용해야한다.

    # 현재 money원 일때 동전의 갯수보다 작은 경우의 동전 갯수는 확인할 필요 없기 때문에 바로 return
    if check[money] >= cnt:  # 이해안됨 ->작으면 그냥 시행 하지마
        return

    # 현재 돈이 x원 이라면
    if money == X:
        # 현재 돈이 x원인 경우가 여러가지 일 수 있는데,
        # 위에서 이전에 money원 일때 동전의 갯수보다 작은경우는 return 했기 때문에
        # 위의 조건을 통과해서 money == X 라는 것은 현재 상태가 동전을 최대한 사용했다는 것이므로
        # money원 일때의 동전의 갯수를 현재 사용한 동전의 갯수(cnt)로 변경해준다.
        check[money] = cnt
        # 결과 동전의 값을 현재 사용한 1,5,10,25 센트 동전의 갯수로 변경
        for i in range(4):
            ans[i] = used[i]
        return






    # 1원 부터 많이 쓰게 시작을 한다
    # 처음 dfs 시작 전에 이미 최소 필요한 1센트 동전의 갯수는 세놨기 때문에
    # 1센트를 5개식(5원씩) 더해도 무방하다
    if coin[0] >= used[0] + 5 and money + 5 <= X:
        used[0] += 5  # 1센트 동전 5개 사용
        dfs(money + 5, cnt + 5)  # 5(1센트 5개) 증가, 동전 5개 사용
        used[0] -= 5  # 사용한 1센트 동전 되돌리기 ? 왜 되돌릴까 실패해서 리턴안대서 돌아옴
    # 5센트 동전 사용
    if coin[1] >= used[1] and money + 5 <= X:
        used[1] += 1  # 5센트 동전 1개 사용
        dfs(money + 5, cnt + 1)  # 5원(5센트 X 1) 증가, 동전 1개 사용
        used[1] -= 1  # 사용한 5센트 동전 되돌리기
        # 10센트 동전 사용
    if coin[2] >= used[2] and money + 10 <= X:
        used[2] += 1  # 10센트 동전 1개 사용
        dfs(money + 10, cnt + 1)  # 10원(10센트 X 1) 증가, 동전 1개 사용
        used[2] -= 1  # 사용한 10센트 동전 되돌리기
        # 25센트 동전 사용
    if coin[3] >= used[3] and money + 25 <= X:
        used[3] += 1  # 25센트 동전 1개 사용
        dfs(money + 25, cnt + 1)  # 25원(25센트 X 1) 증가, 동전 1개 사용
        used[3] -= 1  # 사용한 25센트 동전 되돌리기



if __name__ == '__main__':

    coin = [0] * 4  # 1,5,10,25 동전 갯수, 총 갯수
    ans = [0] * 4  # 정답 1,5,10,25 동전 갯수, 사용한 갯수
    check = [-1] * 10001  # check[i] = x: i 원을 만들기 위해 최대로 사용한 동전의 개수 x
    used = [0] * 4  # 사용한 1,5,10,25 동전 개수

    # 입력
    X, coin[0], coin[1], coin[2], coin[3] = map(int, input().split())

    x = X % 5  # 필요한 1 센트 갯수 확인

    if coin[0] < x:  # 현재 가지고 있는 1센트 x 보다 작으면 무조건 불가능
        print(0, 0, 0, 0)
        exit(0)  # 프로그램 종료

    # # X까지 사용하게 되므로 -1로 초기화, 0으로 하게되면 동전을 1개도 사용하지 않을때와 겹쳐서 0이하의 숫자로 해야한다
    # for i in range(X + 1):
    #     check[i] = -1

    # x개의 1센트 동전은 반드시 사용용하게 다, 따라서 사용한 1센트 동전(used[0])과 처음 식작하게 되는 돈을 x 로 초기화
    used[0], money = x, x

    # 시작 돈 : ㅌdnjs 시작 동전의 갯수 : x개
    dfs(money, money)
    # 결과 동전의 갯수 출력
    print(*ans)



def dfs(money, cnt):  # money: 현재까지의 동전의 합 cnt : 현재까지의 동전의 갯수
    # 동전을 최대한으로 사용해야 한다.
    # 현재 돈(money)원 일때 동전의 갯수보다 작은 경우의 동전 갯수는 확인할 필요 없기 때문에 바로 return
    if check[money] >= cnt:
        return
    # 현재 돈이 X원 이라면
    if money == X:
        # 현재 돈이 X원인 경우가 여러가지 일 수 있는데,
        # 위에서 이전에 money원 일때 동전의 갯수보다 작은 경우는 return 했기 때문에
        # 위의 조건을 통과해서 money == X 라는 것은 현재 상태가 동전을 최대한 사용했다는 것이므로
        # money원 일때의 동전의 갯수를 현재 사용한 동전의 갯수(cnt)로 변경해준다.
        check[money] = cnt
        # 결과 동전의 값을 현재 사용한 1, 5, 10, 25 센트 동전의 갯수로 변경
        for i in range(4):
            ans[i] = used[i]
        return
    # money원일 때 사용한 최대 동전의 갯수
    check[money] = cnt
    # 처음 dfs 시작 전에 이미 최소 필요한 1센트 동전의 갯수는 세놨기 때문에
    # 1센트를 5개씩(5원씩) 더해도 무방하다.
    if coin[0] >= used[0] + 5 and money + 5 <= X:
        used[0] += 5  # 1센트 동전 5개 사용
        dfs(money + 5, cnt + 5)  # 5원(1센트 X 5) 증가, 동전 5개 사용
        used[0] -= 5  # 사용한 1센트 동전 되돌리기
    # 5센트 동전 사용
    if coin[1] > used[1] and money + 5 <= X:
        used[1] += 1  # 5센트 동전 1개 사용
        dfs(money + 5, cnt + 1)  # 5원(5센트 X 1) 증가, 동전 1개 사용
        used[1] -= 1  # 사용한 5센트 동전 되돌리기
    # 10센트 동전 사용
    if coin[2] > used[2] and money + 10 <= X:
        used[2] += 1  # 10센트 동전 1개 사용
        dfs(money + 10, cnt + 1)  # 10원(10센트 X 1) 증가, 동전 1개 사용
        used[2] -= 1  # 사용한 10센트 동전 되돌리기
    # 25센트 동전 사용
    if coin[3] > used[3] and money + 25 <= X:
        used[3] += 1  # 25센트 동전 1개 사용
        dfs(money + 25, cnt + 1)  # 25원(25센트 X 1) 증가, 동전 1개 사용
        used[3] -= 1  # 사용한 25센트 동전 되돌리기

#
# if __name__ == '__main__':
#     coin = [0] * 4  # 1, 5, 10, 25 센트 동전 갯수
#     ans = [0] * 4  # 정답 1, 5, 10, 25 센트 동전 갯수
#     check = [-1] * 10001  # check[i] = x : i원을 만들기 위해 최대로 사용한 동전의 개수 x
#     used = [0] * 4  # 사용한 1, 5, 10, 25 센트 동전 갯수
#
#     X, coin[0], coin[1], coin[2], coin[3] = map(int, sys.stdin.readline().split())
#
#     x = X % 5  # 필요한 1센트 갯수 확인
#     if coin[0] < x:  # 현재 가지고 있는 1센트가 x보다 작으면 무조건 불가능
#         print(0, 0, 0, 0)
#         exit(0)
#
#     # x개의 1센트 동전은 반드시 사용하게 된다. 따라서 사용한 1센트 동전(used[0]) 과 처음 시작하게 되는 돈을 x로 초기화
#     used[0], money = x, x
#     dfs(money, money)  # 시작 돈 : x원 시작 동전의 갯수 : x개
#
#     # 결과 동전의 갯수 출력
#     for y in ans:
#         print(y, end=' ')
