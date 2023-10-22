import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().strip().split())
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
board = []
for _ in range(r):
    board.append(list(input().strip()))

for i in range(r):
    print(board[i])


def find_swans():
    swan = []
    for y in range(r):
        for x in range(c):
            if board[y][x] == "L":
                swan.append((y, x))
    return swan


def melt():
    q = deque()
    for y in range(r):
        for x in range(c):
            if board[y][x] == "X":
                for dy, dx in d:
                    Y = dy + y
                    X = dx + x
                    if 0 <= Y < r and 0 <= X < c and board[Y][X] == ".":
                        q.append((y, x))
                        break
    while q:
        y, x = q.popleft()
        board[y][x] = "."


def init():
    swans = find_swans()
    swan = swans[0]
    another_swan = swans[1]
    s_y, s_x = swan
    visited = [[0] * c for _ in range(r)]
    q = deque()
    q.append((s_y, s_x))
    visited[s_y][s_x] = 1

    return q, another_swan, visited


def find_max_indices(matrix):
    max_indices = {}
    max_value = float("-inf")  # 음의 무한대로 초기화

    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_indices = {(row_idx, col_idx)}
            elif value == max_value:
                max_indices.add((row_idx, col_idx))

    return max_indices


def check(q, another_swan, visited, max_idx):
    f_y, f_x = another_swan

    for y in range(r):
        for x in range(c):
            if visited[y][x] == max_idx:
                q.append((y, x))
    while q:
        y, x = q.popleft()
        max_idx = visited[y][x]
        if y == f_y and x == f_x:
            return True
        for dy, dx in d:
            Y = dy + y
            X = dx + x
            if (
                0 <= Y < r
                and 0 <= X < c
                and board[Y][X] == "."
                and visited[Y][X] < visited[y][x]
            ):
                visited[Y][X] = visited[y][x] + 1


while 1:
    cnt = 0
    # 빙하 녹음
    melt()
    # 백조 만날 수 있는 지 bfs로 체크
    q, another_swan, visited = init()
    flag = check(q, another_swan, visited)
    if flag:
        print(cnt)
        break
    cnt += 1
