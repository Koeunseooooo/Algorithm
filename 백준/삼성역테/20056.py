import sys

input = sys.stdin.readline

n, mm, k = map(int, input().strip().split())
board = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(mm):
    r, c, m, s, d = map(int, input().strip().split())
    board[r - 1][c - 1].append((m, s, d))

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# for i in range(len(board)):
#     print(board[i])

# print()
for _ in range(k):
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 0:
                for fire in board[i][j]:
                    m, s, d_idx = fire
                    y, x = i, j
                    # print(y, x, "before")
                    dy, dx = d[d_idx]
                    Y = y + dy * s
                    X = x + dx * s
                    while Y < 0:
                        Y += n
                    while X < 0:
                        X += n
                    Y = Y % n
                    X = X % n
                    # print(Y, X, "after")
                    # board[i][j].remove(fire)
                    temp[Y][X].append(fire)
    board = temp[:]
    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                cnt = len(board[i][j])
                sum_m = sum(col[0] for col in board[i][j])
                sum_s = sum(col[1] for col in board[i][j])
                # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
                # board[i][j] = []
                new_m = sum_m // 5
                new_s = sum_s // cnt
                if new_m == 0:
                    board[i][j] = []
                    continue
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 방향은 0, 2, 4, 6이 되고,
                # 그렇지 않으면 1, 3, 5, 7이 된다.
                index_2_values = [item[2] for item in board[i][j]]
                result = all(x % 2 == index_2_values[0] % 2 for x in index_2_values)
                board[i][j] = []
                if result:  # 0,2,4,6
                    for new_d in range(0, 7, 2):
                        board[i][j].append((new_m, new_s, new_d))
                else:  # 1,3,5,7
                    for new_d in range(1, 8, 2):
                        board[i][j].append((new_m, new_s, new_d))


# for i in range(len(board)):
#     print(board[i])

# 모든 값의 합을 저장할 변수 초기화
total_sum = 0

# 중첩된 반복문을 사용하여 모든 값 더하기
for i in range(len(board)):
    for j in range(len(board)):
        if len(board[i][j]) > 1:
            tmp_sum = sum(col[0] for col in board[i][j])
            total_sum += tmp_sum
        elif len(board[i][j]) == 1:
            total_sum += board[i][j][0][0]

print(total_sum)
