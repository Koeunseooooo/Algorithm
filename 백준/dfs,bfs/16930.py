from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, K = map(int, input().split())  # N:세로 M:가로, K: step
graph = [list(input().strip()) for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
check = [[INF] * M for _ in range(N)]


def bfs():
    global sx, sy, ex, ey
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((sx, sy))
    check[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for dy, dx in d:
            nx, ny = x + dx, y + dy
            nk = 1
            while (
                nk <= K
                and 0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] != "#"
                and check[nx][ny] > check[x][y]  # point
            ):
                if check[nx][ny] == INF:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1
                nx += dx
                ny += dy
                nk += 1


bfs()
if check[ex][ey] == INF:
    print(-1)
else:
    print(check[ex][ey])
