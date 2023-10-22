import sys
from collections import deque

input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 남 동 북 서 (반시계방향)
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().strip().split())
    y -= 1
    x -= 1
    board[y][x] = "a"

l = int(input())
dirs = []
for _ in range(l):
    t, c = input().strip().split()
    t = int(t)
    dirs.append((t, c))


# init
cur_t = 0
cur_idx = 1  # 처음에 동쪽을 바라보고 있음
board[0][0] = 1
y = 0
x = 0
tail = deque()
tail.append((y, x))

while 1:
    cur_t += 1
    dy, dx = d[cur_idx]
    if 0 <= y + dy < n and 0 <= x + dx < n:
        if board[y + dy][x + dx] == 1:  # 자기자신
            break
        else:
            y += dy
            x += dx
            if board[y][x] == 0:  # 사과가 없다면
                board[y][x] = 1
                tail_y, tail_x = tail.popleft()
                board[tail_y][tail_x] = 0
                tail.append((y, x))
            else:
                tail.append((y, x))
                board[y][x] = 1
    else:  # board를 벗어나면
        break
    for t, c in dirs:
        if cur_t == t:
            if c == "L":
                cur_idx = (cur_idx + 4 + 1) % 4
            else:
                cur_idx = (cur_idx + 4 - 1) % 4
print(cur_t)
