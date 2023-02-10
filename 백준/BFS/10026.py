from collections import deque

n = int(input())

graph = []

color = ["R", "G"]

for _ in range(n):
    graph.append(list(input()))

visited = [[0]*n for i in range(n)]
user = 0
rg_user = 0

# 이동할 4가지 방향 정의 (상,하,좌,우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            tmp_x = x+dx[i]
            tmp_y = y+dy[i]

            if tmp_x < 0 or tmp_x >= n or tmp_y < 0 or tmp_y >= n:
                continue

            if not visited[tmp_x][tmp_y]:
                if graph[tmp_x][tmp_y] == graph[x][y]:
                    visited[tmp_x][tmp_y] = 1  # 설마 이거 때문...?
                    queue.append((tmp_x, tmp_y))

    return 1


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            user += bfs(i, j)

visited = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            rg_user += bfs(i, j)

print(user, rg_user)
