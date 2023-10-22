import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip().split())))

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

left = [
    (-2, 0, 0.02),
    (-1, 0, 0.07),
    (-1, 1, 0.01),
    (-1, -1, 0.1),
    (0, -2, 0.05),
    (1, -1, 0.1),
    (1, 0, 0.07),
    (2, 0, 0.02),
    (1, 1, 0.01),
    (0, -1, 0),
]
right = [(y, -x, z) for y, x, z in left]
down = [(-x, y, z) for y, x, z in left]
up = [(x, y, z) for y, x, z in left]
sand_dir = {0: left, 1: down, 2: right, 3: up}
res = 0


def scatter(board, y, x, d_idx):
    global res
    sand_d = sand_dir[d_idx]
    total = 0
    # print("시작", y, x)
    for dy, dx, rate in sand_d:
        Y = y + dy
        X = x + dx
        if rate == 0:  # a(나머지)
            new_sand = board[y][x] - total
        else:  # 비율
            new_sand = int(board[y][x] * rate)
            total += new_sand

        if 0 <= Y < n and 0 <= X < n:
            board[Y][X] += new_sand
        else:
            res += new_sand

    board[y][x] = 0  # 모든 모래가 이동하므로 기존 칸에 있던 모래는 0이 된다
    return board


def tornado():
    global board
    y = x = int(n / 2)  # 배열의 중앙 좌표
    d_idx = 0
    move_count = 0  # move_count가 2가 될 때마다 길이를 1씩 늘려주어야 함
    dist = 1
    flag = 0

    while True:
        if flag:
            break
        move_count += 1
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = y + dy
            X = x + dx
            if (Y, X) == (0, -1):
                flag = 1
                break
            board = scatter(board, Y, X, d_idx)
            y = Y
            x = X
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0


tornado()

print(res)
