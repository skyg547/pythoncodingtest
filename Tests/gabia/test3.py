def solution(N, coffee_times):
    answer = []

    if N == 1:
        for i in range(len(coffee_times)):
            answer.append(i + 1)

        return answer

    table = []
    t = 0
    index = 1

    for i in range(N):
        table.append([coffee_times[0], t, index])
        index += 1
        coffee_times.pop(0)

    templens = len(table)
    print("temp lens ", templens)

    while table:
        t += 1
        print('t******************************', t, "*************************")

        print(table, 'table 중간점검 ')

        # 지금 들어온 시간 + 커피 타임스 , 인덱스 이렇게 저장 추출
        for i in sorted(table):
            if i[1] + i[0] == t:
                print(i, '0+1', i[1] + i[0], 't ', t)
                answer.append(i[2])
                table.remove(i)
                templens -= 1

        # 3보다 낮으면 더 넣기
        if templens < N:
            for i in coffee_times:
                if templens < N:
                    table.append([coffee_times[0], t, index])
                    index += 1
                    print('cf time = ', coffee_times)
                    coffee_times.pop(0)
                    templens += 1

    return answer


n = 3
c = [7, 4, 1, 5, 3]

print('answer = ', solution(n, c))
