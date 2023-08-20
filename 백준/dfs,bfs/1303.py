from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())


arr = []
for _ in range(m):
    arr.append(list(input().strip()))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    cur = arr[y][x]
    arr[y][x] = 1  # 방문했음을 의미
    cnt = 0  # 시작 ~!
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if (0 <= X < n) and (0 <= Y < m) and arr[Y][X] == cur:
                q.append((Y, X))
                arr[Y][X] = 1
    return cnt


w_cnt = 0
b_cnt = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == "W":
            w_cnt += bfs(i, j) ** 2
        elif arr[i][j] == "B":
            b_cnt += bfs(i, j) ** 2


print(w_cnt)
print(b_cnt)
