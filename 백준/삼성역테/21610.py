n, m = map(int, input().split())
board = []
cloud = [[0] * n for _ in range(n)]
comms = []
for _ in range(n):
    board.append(list(map(int, input().split())))


for _ in range(m):
    comms.append(list(map(int, input().split())))

d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 1,3,5,7은 대각선 방향


def init_cloud():
    global cloud
    init = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
    for y, x in init:
        cloud[y][x] = 1


def print_cloud():  # 구름 위치
    global cloud
    for i in range(len(cloud)):
        print(cloud[i])
    print("-----")


def print_board():  # 물바구니
    global print_board
    for i in range(len(board)):
        print(board[i])
    print("-----")


def move_cloud(d_idx, s):
    global d, cloud
    dy, dx = d[d_idx]
    update_cloud = []
    for y in range(len(cloud)):
        for x in range(len(cloud)):
            if cloud[y][x]:
                Y = y + (dy * s)
                X = x + (dx * s)
                while Y < 0:
                    Y += n
                while X < 0:
                    X += n
                Y = Y % n
                X = X % n
                cloud[y][x] = 0
                update_cloud.append((Y, X))
                # cloud[Y][X] = 1 # 이렇게 구름 접근 과정 중에 바로 업데이트 하면 안 됨 ^^
    for y, x in update_cloud:
        cloud[y][x] = 1


def rain():
    global cloud
    for i in range(len(cloud)):
        for j in range(len(cloud)):
            if cloud[i][j]:
                board[i][j] += 1


def disappear_cloud():
    global cloud
    for i in range(len(cloud)):
        for j in range(len(cloud)):
            if cloud[i][j]:
                cloud[i][j] = 0


def waterCopyBug():
    global cloud
    for y in range(len(cloud)):
        for x in range(len(cloud)):
            if cloud[y][x]:
                cnt = 0
                for i in range(1, 8, 2):
                    dy, dx = d[i]
                    Y = y + dy
                    X = x + dx
                    if 0 <= Y < n and 0 <= X < n and board[Y][X] > 0:
                        cnt += 1
                board[y][x] += cnt


def appear_cloud():
    global cloud
    new_cloud = []
    for i in range(len(cloud)):
        for j in range(len(cloud)):
            if not cloud[i][j]:
                if board[i][j] >= 2:
                    new_cloud.append((i, j))
                    board[i][j] -= 2
    disappear_cloud()
    for y, x in new_cloud:
        cloud[y][x] = 1


init_cloud()
for i in range(m):
    d_idx, s = comms[i]
    move_cloud(d_idx - 1, s)
    rain()
    waterCopyBug()
    appear_cloud()
    # print_board()
    # print_cloud()

print(sum(sum(s) for s in board))
