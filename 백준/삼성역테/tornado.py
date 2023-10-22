n = 5
board = [[0] * 5 for _ in range(n)]


dist = 1
d_idx = 0
move_count = 0  # 2가 될때마다 dist가 1커지고 move_count는 0으로 초기화
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

y, x = n // 2, n // 2
board[y][x] = 1
print(y, x)
flag = 0
while True:
    if flag:
        break
    for i in range(dist):
        dy, dx = d[d_idx]
        Y = y + dy
        X = x + dx
        if (Y, X) == (0, -1):
            flag = 1
            break
        board[Y][X] += board[y][x] + 1
        y = Y
        x = X
    d_idx = (d_idx + 1) % 4
    move_count += 1
    if move_count == 2:
        dist += 1
        move_count = 0

for i in range(len(board)):
    print(board[i])
