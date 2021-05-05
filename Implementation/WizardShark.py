from collections import deque

newdir = [[1, 3, 5, 7], [0, 2, 4, 6]]  # 방향 그래프
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  # 이동방향
sharks = deque()

# Initialize
N, M, K = map(int, input().split())

# 판
board = list(list(deque() for _ in range(N)) for _ in range(N))
print(board)

for i in range(1, M + 1):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append((m, s, d))
    sharks.append([r - 1, c - 1])

print(board)

# Start
for _ in range(K):

    # 돌기전 출력
    print("\nRIGHT BEFORE MOVING")
    for b in board:
        print(*b)

    # 들어가있는 파이어 볼수
    cnt = len(sharks)
    # 파이어 볼수 만큼 반복
    for _ in range(cnt):
        # 위치를 가져와서
        r, c = sharks.popleft()

        #??? ->
        # if not board[r][c]:
        #     continue

        # 속도 질량 이거 끄내오기
        m, s, d = board[r][c].popleft()

        # 이동 벽넘어 가는 부분 세로 먼저, 그다음 가로줄 이동
        nr, nc = (r + dx[d] * s) % N, (c + dy[d] * s) % N

        sharks = deque()
        board = list(list(deque() for _ in range(N)) for _ in range(N))

        # 새로운 파이어볼 위치
        sharks.append([nr, nc])

        # 새로운 속도 무게 위치
        board[nr][nc].append((m, s, d))

    print("\nRIGHT AFTER MOVING:")

    # 이동 후
    for b in board:
        print(b)

    # 보드를 돌것인데
    # 세로 줄
    for i in range(N):
        # 가로줄
        for j in range(N):

            # 만약 파이어볼이 있다면
            if len(board[i][j]) > 1:
                # 새로운 파이어볼 길이 나눠줄 갯수  ?
                num = len(board[i][j])
                # 새로운 질량
                new_mass = 0
                # 새로운 스피드
                new_speed = 0
                # 새로운 방향
                directions = []

                # 보드 i,j 이 있을때
                while board[i][j]:
                    # 거기에 있는 모든 파이어볼들을 뺀다.
                    m, s, d = board[i][j].pop()
                    # 질량은 더해주고
                    new_mass += m
                    # 속도도 더해주고
                    new_speed += s
                    # 방향도 더해준다.
                    directions.append(d)

                new_mass //= 5 #질량
                new_speed //= num # 새로운 스피드
                # 새로운 방향인데 모든 방향이 2 로 나눳을때 홀수거나  # 2로 나눳을때 1ㅊ이면 false 와 true 로 반환 해준다
                new_direction = all(list(map(lambda x: x % 2 == 0, directions))) | all(list(map(lambda x: x % 2 == 1, directions)))
                # 질량이 0이 아니면
                if new_mass != 0:
                    # 4개르 를 추가 해주는데
                    for idx in range(4):
                        # 방향이랑 다 추가해준다 .
                        board[i][j].append((new_mass, new_speed, newdir[new_direction][idx]))
                        sharks.append([i, j])

    print("\nAFTER COMBINATION")

    for b in board:
        print(b)

ans = 0

# 판을 돌면서
for i in range(N):

    for j in range(N):
        # 판이 있을 때 까지
        while board[i][j]:


            m,s,d = board[i][j].pop()
            ans += m

print(ans)
