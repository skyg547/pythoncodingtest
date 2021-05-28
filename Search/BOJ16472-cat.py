# https://www.acmicpc.net/problem/16472
# 고냥이


# def solution(s, l):
#     # 작고
#     index1, index2 = 0, len(l)
#     temp = set([])
#
#     for i in l:
#         if len(temp) <= 1:
#             temp.add(i)
#         else:
#             temp.pop()
#     print(temp)
#
#
# if __name__ == '__main__':
#     s = 2
#     l = 'abbcaccba'
#     print(solution(s, l))

import sys
from collections import deque

if __name__ == '__main__':
    n = int(input())
    s = input()

    # 알파벳 개수 세기
    check = [0] * 26
    # 배열의 크기 인덱스 벗어나면 안되니
    size = len(s)
    # 투포인터 , 오른쪽부터 검색 그담음 왼쪽 증가
    left, right = 0, 0
    # tmp = 인식한 문자 개수, ans = 현재 길이답
    ans, tmp = 0,0
    # 현재 인식한 문자열 큐
    q = deque()

    # 왼쪽 과 오른쪽은 인덱스 벗어나면 안대고
    while left < size and right <size:
        # 오른쪽이 인덱스 벗어 나지않는 선에서
        while right < size:
            # 인식한 문자가 2개 이거나 새로운문자가 들어 올라고 한다면
            if tmp == n and not check[ord(s[right])-ord('a')]:
                break # 취소

            # 인식 한 문자가 없던 문자면 하나 추가
            if not check[ord(s[right])- ord('a')]:
                tmp += 1

            # 현재 문자열에 하나있다고 추가
            check[ord(s[right])-ord('a')] += 1
            #  큐에 넣고
            q.append(s[right])
            # 오른쪽 증가
            right += 1

        # 최장거리 답변 최신화
        ans = max(ans,len(q))
        # 큐에서 가장 앞에 있는
        first = q[0]
        # 문자열 하나 빼줘서 감소
        check[ord(first)-ord('a')] -= 1
        # 빼주기
        q.popleft()
        # 만약 그 문자가 문자열이 하나 도 없다면
        if not check[ord(first) - ord('a')]:
            # 인식한 그걸 감소
            tmp -= 1
        # 왼쪽 포인터를 올려준다 .
        left += 1

    print(ans)