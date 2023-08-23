# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().strip().split())

# arr = [list(map(int, input().split())) for _ in range(n)]


# # 인접 방향(대각선 포함)
# d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


# def bfs(y, x):
#     q = deque()
#     q.append((y, x))
#     cnt = 0
#     visited = [[0] * m for _ in range(n)]
#     isShark = 0  # flag
#     while q:
#         y, x = q.popleft()
#         for dy, dx in d:
#             Y = y + dy
#             X = x + dx
#             if 0 <= X < m and 0 <= Y < n and visited[Y][X] == 0:
#                 if arr[Y][X] == 0:
#                     q.append((Y, X))
#                     visited[Y][X] = cnt + 1
#         cnt += 1
#         if isShark:
#             break
#     return cnt


# ans = 0
# for y in range(n):
#     for x in range(m):
#         if arr[y][x] != 1:
#             if ans < bfs(y, x):
#                 ans = bfs(y, x)

# print(ans)

import sys
from collections import deque

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 상어가 있는 위치에서 탐색하기 위해
            dq.append([i, j])

result = 0
# 상어 있는 위치 기준으로 최단 거리 구하기
while dq:
    x, y = dq.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] != 0:
            continue
        dq.append([nx, ny])
        graph[nx][ny] = graph[x][y] + 1
        result = max(result, graph[x][y] + 1)
print(result - 1)


# 근데 이거는 내가 푼걸로도 되긴해야하는거 아닌가..?
# 틀렸습니다가 아니라 시간초과가 떠야할 것 같은데 다시 풀어보자
