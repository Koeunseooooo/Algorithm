from collections import deque

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dice = [1, 2, 3, 4, 5, 6]
d_idx = 0  # 초기방향 동쪽
y, x = 0, 0
# 0,1,2,3=동,남,서,북
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def reverse_direction(d_idx):
    if d_idx == 0:
        return 2
    elif d_idx == 1:
        return 3
    elif d_idx == 2:
        return 0
    else:
        return 1


def update_dice(d_idx):  # 방향, 주사위
    global dice
    one, two, three, four, five, six = (
        dice[0],
        dice[1],
        dice[2],
        dice[3],
        dice[4],
        dice[5],
    )
    if d_idx == 0:  # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            four,
            two,
            one,
            six,
            five,
            three,
        )
    elif d_idx == 2:  # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            three,
            two,
            six,
            one,
            five,
            four,
        )
    elif d_idx == 3:  # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            five,
            one,
            three,
            four,
            six,
            two,
        )
    elif d_idx == 1:  # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            two,
            six,
            three,
            four,
            one,
            five,
        )


def move_dice():
    global y, x, d_idx
    dy, dx = d[d_idx]
    Y = dy + y
    X = dx + x
    if 0 <= Y < n and 0 <= X < m:
        update_dice(d_idx)
        y, x = Y, X
    else:
        d_idx = reverse_direction(d_idx)
        dy, dx = d[d_idx]
        Y = dy + y
        X = dx + x
        update_dice(d_idx)
        y, x = Y, X


def print_dice_info():
    global dice, y, x, d_idx
    print("주사위", dice)
    print("현재 위치", y, x)
    print("현재 방향", d_idx)


def print_board():
    for i in range(len(board)):
        print(board[i])


def get_score():  # bfs()
    global y, x, result
    b = board[y][x]
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        yy, xx = q.popleft()
        for dy, dx in d:
            Y = yy + dy
            X = xx + dx
            if 0 <= Y < n and 0 <= X < m and board[Y][X] == b and not visited[Y][X]:
                visited[Y][X] = 1
                q.append((Y, X))
    c = 0
    for i in range(len(visited)):
        c += visited[i].count(1)
    result += c * b


def decide_direction():
    global dice, d_idx
    a = dice[5]
    b = board[y][x]
    if a > b:
        d_idx = (d_idx + 1) % 4
    elif b > a:
        d_idx = (d_idx - 1 + 4) % 4


result = 0
for _ in range(k):
    move_dice()
    get_score()
    decide_direction()
print(result)
