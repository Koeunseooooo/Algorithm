import sys
from collections import deque

input = sys.stdin.readline


d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
n, m = map(int, input().strip().split())
r, c, d_idx = map(int, input().strip().split())
# 0 : 청소되지 않은 빈칸
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))

cnt = 0

while 1:
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    flag = 0
    for dy, dx in d:
        if 0 <= r + dy < n and 0 <= c + dx < m and arr[r + dy][c + dx] == 0:
            flag = 1
            break
    if not flag:
        dy, dx = d[d_idx]
        if 0 <= r - dy < n and 0 <= c - dx < m and arr[r - dy][c - dx] != 1:  # 후진 가능
            r -= dy
            c -= dx
            continue
        else:
            break
    else:
        d_idx = (d_idx + 4 - 1) % 4
        dy, dx = d[d_idx]
        if 0 <= r + dy < n and 0 <= c + dx < m and arr[r + dy][c + dx] == 0:
            r += dy
            c += dx
print(cnt)
