# 상하좌우 1이있으면 갈 곳이 있다는 뜻이고,
# 본인은 계속 누적해서 움직이면 됨
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))


d = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if (0 <= Y < n) and (0 <= X < m) and arr[Y][X] == 1:
                q.append((Y, X))
                arr[Y][X] = arr[y][x] + 1  # 방문 및 현재까지 지나간 칸 수를 의미


bfs(0, 0)
print(arr[n - 1][m - 1])
